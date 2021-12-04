#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=1
#SBATCH --time=48:00:00
#SBATCH --output=train-%J.out
#SBATCH --error=train-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source ~/.cache/pypoetry/virtualenvs/kolb-poetry-SgAmqU3s-py3.6/bin/activate
fairseq-hydra-train \
    task.data=/home/tkolb/bsc/data/ctc2tempdata3 \
    model.w2v_path=/home/tkolb/bsc/data/models/wav2vec_small.pt \
    model.freeze_finetune_updates=10000 \
    --config-dir /home/tkolb/bsc/bsc-thesis/scripts/fairseq \
    --config-name base_10h_custom
deactivate