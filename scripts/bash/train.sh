#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=10G
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --output=train-%J.out
#SBATCH --error=train-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
fairseq-hydra-train \
    task.data="/home/tkolb/bsc/outputdata" \
    model.w2v_path="/home/tkolb/bsc/models/wav2vec_small.pt" \
    --config-dir "/home/tkolb/bsc/bsc-thesis/scripts/fairseq" \
    --config-name base_100h_custom
deactivate