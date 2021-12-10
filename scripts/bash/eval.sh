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

datetime1="2021-12-03/14-49-23"
datetime2="2021-12-08/19-47-17"
datetime3="2021-12-06/15-48-32"
valid_data_path="/home/tkolb/bsc/data/ctc2tempdata3"
lmfile="c2lmfile.bin"
lexicon="c2lexicon.txt"
gen_subset="test"
outputsfolder="fairseq-xlsr-outputs"
evalsfolder="fairseq-xlsr-evals"

source ~/.cache/pypoetry/virtualenvs/thomas-poetry-yCU5QAa0-py3.8/bin/activate
python3 ~/bsc/fairseq/examples/speech_recognition/infer.py \
    $valid_data_path \
    --task audio_finetuning \
    --nbest 1 \
    --path ~/bsc/data/$outputsfolder/$datetime1/checkpoints/checkpoint_best.pt \
    --gen-subset $gen_subset \
    --results-path ~/bsc/data/$evalsfolder/$datetime1/$gen_subset \
    --w2l-decoder kenlm \
    --lm-model ~/bsc/data/models/$lmfile \
    --lm-weight 2 \
    --lexicon ~/bsc/data/models/$lexicon \
    --word-score 2 \
    --sil-weight 0 \
    --criterion ctc \
    --labels ltr \
    --max-tokens 1000000 \
    --post-process letter
python3 ../extractWER.py "/home/tkolb/bsc/data/$evalsfolder/$datetime1/$gen_subset" $valid_data_path
python3 ~/bsc/fairseq/examples/speech_recognition/infer.py \
    $valid_data_path \
    --task audio_finetuning \
    --nbest 1 \
    --path ~/bsc/data/$outputsfolder/$datetime2/checkpoints/checkpoint_best.pt \
    --gen-subset $gen_subset \
    --results-path ~/bsc/data/$evalsfolder/$datetime2/$gen_subset \
    --w2l-decoder kenlm \
    --lm-model ~/bsc/data/models/$lmfile \
    --lm-weight 2 \
    --lexicon ~/bsc/data/models/$lexicon \
    --word-score 2 \
    --sil-weight 0 \
    --criterion ctc \
    --labels ltr \
    --max-tokens 1000000 \
    --post-process letter
python3 ../extractWER.py "/home/tkolb/bsc/data/$evalsfolder/$datetime2/$gen_subset" $valid_data_path
python3 ~/bsc/fairseq/examples/speech_recognition/infer.py \
    $valid_data_path \
    --task audio_finetuning \
    --nbest 1 \
    --path ~/bsc/data/$outputsfolder/$datetime3/checkpoints/checkpoint_best.pt \
    --gen-subset $gen_subset \
    --results-path ~/bsc/data/$evalsfolder/$datetime3/$gen_subset \
    --w2l-decoder kenlm \
    --lm-model ~/bsc/data/models/$lmfile \
    --lm-weight 2 \
    --lexicon ~/bsc/data/models/$lexicon \
    --word-score 2 \
    --sil-weight 0 \
    --criterion ctc \
    --labels ltr \
    --max-tokens 1000000 \
    --post-process letter
python3 ../extractWER.py "/home/tkolb/bsc/data/$evalsfolder/$datetime3/$gen_subset" $valid_data_path
deactivate