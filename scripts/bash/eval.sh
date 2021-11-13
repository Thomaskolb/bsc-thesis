#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=1
#SBATCH --time=6:00:00
#SBATCH --output=eval-%J.out
#SBATCH --error=eval-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

datetime="2021-11-11/18-12-54"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ../extractWER.py "/home/tkolb/bsc/data/fairseq-evals/$datetime"
deactivate