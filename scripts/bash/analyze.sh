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

datetime1="2021-12-16/12-12-56"
datetime2="2021-12-16/12-15-36"
datetime3="2021-12-12/11-41-57" 
basepath="/home/tkolb/bsc/data/fairseq-evals-xlsr/opt"
outfolder="/home/tkolb/bsc/data/analysis-xlsr/summary"
gen_subset="test"

source ~/.cache/pypoetry/virtualenvs/tkolbpoetry-0grRN4_Q-py3.6/bin/activate
python3 ../analyzecaptions.py "$outfolder/xlsrs8.txt" \
    "$basepath/$datetime1/$gen_subset"
python3 ../analyzecaptions.py "$outfolder/xlsrs16.txt" \
    "$basepath/$datetime2/$gen_subset"
python3 ../analyzecaptions.py "$outfolder/xlsrs32.txt" \
    "$basepath/$datetime3/$gen_subset"
deactivate