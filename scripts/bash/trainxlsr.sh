#!/bin/bash -e
#SBATCH --partition=das
#SBATCH --gres=gpu:rtx_3090:4
#SBATCH --mem=50G
#SBATCH --cpus-per-task=1
#SBATCH --time=48:00:00
#SBATCH --output=trainxlsr-%J.out
#SBATCH --error=trainxlsr-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
HYDRA_FULL_ERROR=1 fairseq-hydra-train \
    task.data=/home/tkolb/bsc/data/c2tempdata \
    model.w2v_path=/home/tkolb/bsc/data/models/xlsr_53_56k.pt \
    model.freeze_finetune_updates=0 \
    --config-dir /home/tkolb/bsc/bsc-thesis/scripts/fairseq \
    --config-name xlsr
deactivate