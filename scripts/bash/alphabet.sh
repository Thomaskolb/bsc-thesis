#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --time=0:15:00
#SBATCH --output=alphabet-%J.out
#SBATCH --error=alphabet-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source ~/.cache/pypoetry/virtualenvs/thomas-poetry-yCU5QAa0-py3.8/bin/activate
python3 ../extractalphabet.py "/home/tkolb/bsc/data/c3tempdata3/train.ltr" "/home/tkolb/bsc/data/c3tempdata3/dict.ltr.txt"
deactivate
