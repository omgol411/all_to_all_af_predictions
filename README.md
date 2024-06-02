# Pairwise AlphaFold predictions
- ```fragments.txt``` has the sequence fragments of different proteins
- ```generate_pairwise_fasta.py``` generates fasta files for all pairwise combinations in ```fragments.txt``` and stores them in ```fasta_files``` directory
- Structure predictions for all of them can be obtained using ```colabfold_run.py``` (LocalColabFold is required)

# Requirements
- LocalColabFold v1.5.5
