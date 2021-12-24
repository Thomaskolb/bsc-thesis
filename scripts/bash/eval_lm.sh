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

source ~/.cache/pypoetry/virtualenvs/new-env-xry5bPeK-py3.8/bin/activate
python3.8 ../extractWER.py "/ceph/csedu-scratch/other/david/thomas/np" "/home/tkolb/bsc/data/ctc2tempdata" "8h.txt" "/home/tkolb/bsc/data/fairseq-evals-xlsr/ctc2/np"
python3.8 ../extractWER.py "/ceph/csedu-scratch/other/david/thomas/np" "/home/tkolb/bsc/data/ctc2tempdata" "16h.txt" "/home/tkolb/bsc/data/fairseq-evals-xlsr/ctc2/np"
python3.8 ../extractWER.py "/ceph/csedu-scratch/other/david/thomas/np" "/home/tkolb/bsc/data/ctc2tempdata" "32h.txt" "/home/tkolb/bsc/data/fairseq-evals-xlsr/ctc2/np"
deactivate