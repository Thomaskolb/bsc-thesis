#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --output=lmplease-%J.out
#SBATCH --error=lmplease-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

~/bsc/data/kenlm/build/bin/lmplz --discount_fallback -o 5 < ~/bsc/data/models/lmfile.txt > ~/bsc/data/models/lmfile.arpa
~/bsc/data/kenlm/build/bin/build_binary ~/bsc/data/models/lmfile.arpa ~/bsc/data/models/lmfile.bin