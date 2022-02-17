#!/bin/bash
#SBATCH --job-name=lm-summarize
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --tasks-per-node=2
#SBATCH --gres gpu:2
#SBATCH -p 'jsteinhardt'
#SBATCH -w 'smaug'

# module load tensorflow/1.15.0-gpu-py37
TF_CPP_MIN_LOG_LEVEL=3
pipenv run mpiexec -n 2 python3.7 -c 'import sys; import pickle; pickle.loads(open("/tmp/pickle_fn", "rb").read())()'
