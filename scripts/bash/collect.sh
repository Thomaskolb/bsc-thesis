#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --output=collect-%J.out
#SBATCH --error=collect-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

basepath="/home/tkolb/bsc/data/c2tempdata"
pattern=" uh "
lookintofile="asr-train.txt"

grep -n "$pattern" "$basepath/$lookintofile" > "$basepath/collected.txt"
source ~/.cache/pypoetry/virtualenvs/thomas-poetry-yCU5QAa0-py3.8/bin/activate
python3 ../patterncollector.py $basepath
deactivate