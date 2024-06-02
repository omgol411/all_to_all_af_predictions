# Pairwise AlphaFold predictions
- ```fragments.txt``` has the sequence fragments of different proteins
- ```generate_pairwise_fasta.py``` generates fasta files for all pairwise combinations in ```fragments.txt``` and stores them in ```fasta_files``` directory
- Structure predictions for all of them can be obtained using ```colabfold_run.py``` (LocalColabFold is required)

# Requirements
- LocalColabFold v1.5.5 (Refer to https://github.com/YoshitakaMo/localcolabfold for installation)

# Citations
- Mirdita M, Schütze K, Moriwaki Y, Heo L, Ovchinnikov S and Steinegger M. ColabFold - Making protein folding accessible to all.
  Nature Methods (2022) doi: [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1)
- Jumper et al. "Highly accurate protein structure prediction with AlphaFold."
  Nature (2021) doi: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)
- Evans et al. "Protein complex prediction with AlphaFold-Multimer."
  BioRxiv (2022) doi: [10.1101/2021.10.04.463034v2](https://doi.org/10.1101/2021.10.04.463034v2)
