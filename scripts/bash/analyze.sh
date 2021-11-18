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
date="2021-11-11/18-12-54"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ../gathercaptions.py "/home/tkolb/bsc/data/analysis/gathered_captions_interpunction.txt" \
    "$basepath/2021-11-11/18-12-54" \
    "$basepath/2021-11-12/10-12-27" \
    "$basepath/2021-11-12/10-34-58" \
    "$basepath/2021-11-14/15-14-42" \
    "$basepath/2021-11-14/15-23-43" \
    "$basepath/2021-11-14/15-30-40" \
    "$basepath/2021-11-15/11-44-06" \
    "$basepath/2021-11-15/11-45-07" \
    "$basepath/2021-11-15/13-23-43"
deactivate