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

datetime="2021-10-30/15-44-20"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ~/bsc/fairseq/examples/speech_recognition/infer.py \
    ~/bsc/outputdata \
    --task audio_finetuning \
    --nbest 1 \
    --path ~/bsc/data/fairseq-outputs/$datetime/checkpoints/checkpoint_best.pt \
    --gen-subset test \
    --results-path ~/bsc/data/fairseq-evals/$datetime \
    --w2l-decoder kenlm \
    --lm-model /path/to/kenlm.bin \
    --lm-weight 2 \
    --word-score -1 \
    --sil-weight 0 \
    --criterion ctc \
    --labels ltr \
    --max-tokens 4000000 \
    --post-process letter
deactivate