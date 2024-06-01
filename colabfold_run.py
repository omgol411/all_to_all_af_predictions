## This script can be used to run local colabfold ##
## Please go through the brief information about local colabfold given - https://wakeful-talk-e86.notion.site/local-ColabFold-72425fb5c373471db76a2a90b3158bde?pvs=4 ##
## OMG-10/04/2024 ##

import os
from pathlib import Path

input_fasta = "./fasta_files" # specify path to the fasta/a3m file or provide a path to the directory containing fasta files 
output_dir = "./output_models" # specify path to the output directory
Path(output_dir).mkdir(parents=True, exist_ok=True)
pair_mode = "unpaired_paired" # paired , unpaired , unpaired_paired
msa_mode = "mmseqs2_uniref_env" # mmseqs2_uniref_env , mmseqs2_uniref , single_sequence
custom_template_path = "None" # specify path to the directory containg the PDB files
num_recycle = "3" # can be set till 20 (will increase prediction time, ColabFold default value is 3)
num_seeds = "1" # to generate more than one model from each NN
random_seed = "9" 
num_models = "5" # how many NN to use (upto 5; ColabFold default is 5)
model_type = "auto" # auto , alphafold2 , alphafold2_ptm , alphafold2_multimer_v1 , alphafold2_multimer_v2 , alphafold2_multimer_v3, deepfold_v1
max_msa = "8:16" # set as 'max-seq:max-extra-seq' (lower values will sample alternate conformations, read https://elifesciences.org/articles/75751)
num_relax = "1"



#os.system("colabfold_batch -h")
os.system(
'colabfold_batch '
f'{input_fasta} '
f'{output_dir} '
f'--pair-mode {pair_mode} '
f'--msa-mode {msa_mode} '
f'--num-recycle {num_recycle} '
f'--num-seeds {num_seeds} '
#f'--templates '
#f'--custom-template-path {custom_template_path} '
f'--random-seed {random_seed} '
f'--num-models {num_models} '
f'--model-type {model_type} '
#f'--max-msa {max_msa} '
#f'--amber '
#f'--num-relax {num_relax} '
#f'--use-gpu-relax '
f'--overwrite-existing-results '
#f'--save-recycles '
)
