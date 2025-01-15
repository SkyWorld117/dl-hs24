# ETHz Deep Learning 2024 HS

This repository contains the code for the course project of the ETHz Deep Learning 2024 HS. The project focuses on biology-inspired methods against catastrophic forgetting and loss of plasticity. 

NOTE! Please see https://github.com/bitmorse/dl-hs24 for latest plots in /plots directory.

## TODO

### Stage 1
- [x] Incremental training session logic with generic call to train any given model.
- [x] CF metrics computation and aggregation
- [x] Baseline model training inside incremental training WITHOUT replay buffer (i.e. samples from base train set)
- [x] Baseline model training inside incremental training WITH replay buffer
- [x] Implementing GA
- [x] Parameterize population selection in GA
- [x] Implementing SNN
- [x] wrap GA with TrainingSessionInterface
- [x] wrap SNN with TrainingSessionInterface


### Stage 2
- [x] Tuning hyperparameters of GA
- [x] Tuning hyperparameters of SNN
- [x] Implementing visualization of training/evolution

### Stage 3
- [x] Generalization of results over different datasets


## Assumptions
We have 1 base train/test.

We fix the model architecture and hyperparameters.

We have N successive training sessions:

- at each training session our incremental dataset only contains 1 (or more) class. 
- a training session starts at the previous sessions weights.
- the training session happens with whatever training algorithm (baseline, GA, snn....)
- the session ends by computing the CF metrics from the paper

Metrics are collected for all sessions and show how fast forgetting happens as new classes are learned.

## References
- https://ojs.aaai.org/index.php/AAAI/article/download/11651/11510


## Development Pipeline
1. Add desire feature/changes to the TODO list
2. Create a new branch for the feature/changes
3. Implement the feature/changes
4. Create a pull request to merge the changes to the main branch
5. Review the changes and merge the pull request
6. Delete the branch

