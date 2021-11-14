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

datetime="2021-11-12/10-12-27"
valid_data_path="/home/tkolb/bsc/data/tempdata2"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ~/bsc/fairseq/examples/speech_recognition/infer.py \
    $valid_data_path \
    --task audio_finetuning \
    --nbest 1 \
    --path ~/bsc/data/fairseq-outputs/$datetime/checkpoints/checkpoint_best.pt \
    --gen-subset test \
    --results-path ~/bsc/data/fairseq-evals/$datetime \
    --w2l-decoder kenlm \
    --lm-model ~/bsc/data/models/lmfile.bin \
    --lm-weight 2 \
    --lexicon ~/bsc/data/models/lexicon.txt \
    --word-score -1 \
    --sil-weight 0 \
    --criterion ctc \
    --labels ltr \
    --max-tokens 1000000 \
    --post-process letter
python3 ../extractWER.py "/home/tkolb/bsc/data/fairseq-evals/$datetime" $valid_data_path
deactivate