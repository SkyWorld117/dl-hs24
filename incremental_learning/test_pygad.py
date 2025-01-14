from torchvision import datasets, transforms
from incremental_trainer import IncrementalTrainer
from interfaces import TrainingSessionInterface
from baseline.model import LightningANN
import os
import sys
import torch
from torch import nn
import torch.nn.functional as F
from torchvision import transforms
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
import lightning as L

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from genetic_algorithms.ga import GeneticAlgorithmNN
from genetic_algorithms.model import ANN, train_ann, test_ann
from snn.FashionMNIST.model import MultiStepSNN
import pickle

from sessions import GATrainingSession, BaselineTrainingSession, PyGADTrainingSession


def main():
    dataset_name = 'FashionMNIST'
    data_path=f'/tmp/{dataset_name}'
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.Grayscale(),
        transforms.ToTensor(),
    ])
    train_dt = datasets.FashionMNIST(data_path, train=True, download=True, transform=transform)
    test_dt = datasets.FashionMNIST(data_path, train=False, download=True, transform=transform)

    hyperparameters_session = {
        # 'model_type': ANN,
        'model_type': MultiStepSNN,
        'batch_size': 64,
        'num_epochs': 1,
        'lr': 0.001,
        'num_generations': 100,
        'num_parents_mating': 5,
        'population_size': 1000,
        'parent_selection_type': "sss",
        'keep_parents': -1,
        'K_tournament': 3,
        'crossover_type': "single_point",
        'mutation_type': "random",
        'mutation_percent_genes': 10.0,
        'mutation_by_replacement': False,
        'random_mutation_min_val': -0.1,
        'random_mutation_max_val': 0.1,
        'fitness_batch_size': 1000,
        'slurm': True
    }

    incremental_trainer_config = {
        'replay_buffer_size': 1000,
        'incremental_training_size': 1000,
        'training_sessions': 6,
        'base_classes': [0,1,2,3,4],
        'incremental_classes_total': [5,6,7,8,9],
        'incremental_classes_per_session': 1,
        'enable_progress_bar': not hyperparameters_session['slurm'],
    }

    baseline_session = BaselineTrainingSession(hyperparameters_session) #exchange with your own session trainer
    ga_session = PyGADTrainingSession(hyperparameters_session) #exchange with your own session trainer

    # train GA session
    trainer1 = IncrementalTrainer(ga_session, train_dt, test_dt, 
                                 "/home/zyi/scratch/ETHz/checkpoints", incremental_trainer_config)
    trainer1.train()
    trainer1.save_metrics()

    # train baseline session
    trainer2 = IncrementalTrainer(baseline_session, train_dt, test_dt,
                                    "/home/zyi/scratch/ETHz/checkpoints", incremental_trainer_config)
    trainer2.train()
    trainer2.save_metrics()

    # summarize cf metrics
    print("Baseline vs GA session metrics")
    print(f"Omega All [baseline,ga]: {trainer2.get_cf_metric('omega_all')}, {trainer1.get_cf_metric('omega_all')}")
    print(f"Omega Base [baseline,ga]: {trainer2.get_cf_metric('omega_base')}, {trainer1.get_cf_metric('omega_base')}")
    print(f"Omega New [baseline,ga]: {trainer2.get_cf_metric('omega_new')}, {trainer1.get_cf_metric('omega_new')}")

    # baseline session metrics
    # INFO:root:Omega Base: 0.8416872224963
    # INFO:root:Omega New: 0.9972
    # INFO:root:Omega All: 0.7397220851833579


if __name__ == "__main__":
    main()
