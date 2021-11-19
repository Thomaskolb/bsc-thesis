#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:2
#SBATCH --mem=75G
#SBATCH --cpus-per-task=1
#SBATCH --time=48:00:00
#SBATCH --output=trainxlrs-%J.out
#SBATCH --error=trainxlrs-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
fairseq-hydra-train \
    task.data=/home/tkolb/bsc/data/c2tempdata \
    model.w2v_path=/home/tkolb/bsc/data/models/xlsr_53_56k.pt \
    model.freeze_finetune_updates=0 \
    --config-dir /home/tkolb/bsc/bsc-thesis/scripts/fairseq \
    --config-name xlrs
deactivate