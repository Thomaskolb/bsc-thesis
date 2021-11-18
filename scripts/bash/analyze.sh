#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --output=analyze-%J.out
#SBATCH --error=analyze-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

basepath="/home/tkolb/bsc/data/fairseq-evals"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ../gathercaptions.py "/home/tkolb/bsc/data/analysis/int_low.txt" \
    "$basepath/2021-11-14/15-14-42" \
    "$basepath/2021-11-14/15-23-43" \
    "$basepath/2021-11-14/15-30-40"
deactivate