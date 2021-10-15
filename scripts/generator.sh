#!/bin/bash -e
#SBATCH --partition=csedu
#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --output=filter-%J.out
#SBATCH --error=filter-%J.err
#SBATCH --mail-user=thomaskolb@live.nl
#SBATCH --mail-type=BEGIN,END,FAIL

source "/home/tkolb/bsc/bsc-thesis/env/bin/activate"
python3 samplegenerator.py "/home/tkolb/bsc/bsc-thesis/filtered_data.txt" "/home/tkolb/bsc/thomas/data" "/home/tkolb/bsc/outputdata" 
deactivate
