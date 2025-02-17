# ETHz Deep Learning 2024 HS

This repository contains the code for the course project of the ETHz Deep Learning 2024 HS. The project focuses on biology-inspired methods against catastrophic forgetting and loss of plasticity. 

## Quickstart
1. install requirements.txt
2. to run an experiment: incremental_trainer/test.py (or the other tests scripts for the different algos (test_snn.py, test_pygad.py, etc). Each test script runs a GA vs Baseline or SNN vs Baseline. Set hyperparams in config.py and in the test script itself.
3. to plot the experiment: copy the data generated by test.py into /plots/data (see folder convention!). use the jupyter notebook in /plots to make plots like in the paper. NOTE! Please see https://github.com/bitmorse/dl-hs24 for latest plots in /plots directory.


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

