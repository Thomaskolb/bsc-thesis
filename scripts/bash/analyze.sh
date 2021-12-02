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
gen_subset="test"

source ~/.cache/pypoetry/virtualenvs/thomas-poetry-yCU5QAa0-py3.8/bin/activate
python3 ../analyzecaptions.py "/home/tkolb/bsc/data/analysis/var-analysis/base8.txt" \
    "$basepath/2021-11-14/15-14-42/$gen_subset"
python3 ../analyzecaptions.py "/home/tkolb/bsc/data/analysis/var-analysis/base16.txt" \
    "$basepath/2021-11-14/15-23-43/$gen_subset"
python3 ../analyzecaptions.py "/home/tkolb/bsc/data/analysis/var-analysis/base32.txt" \
    "$basepath/2021-11-14/15-30-40/$gen_subset"
deactivate