# Getting started

This folder contains code and files related to our position-aware side-chain (PASC) features.

## If you want to generate your own PASC features, follow the python code in the jupyter notebook "generate-PASC-embeddings.ipynb". This code starts with SMILES strings of the amino acids and uses rdkit to generate mol objects and fingerprints for each heavy atom.

## If you want to encode peptide sequences:

1. Prepare a text file containing a peptide sequence(s). See "example_sequences.txt" as an example.

2. Run the python script "encoding_with_PASC.py" (example command: "python encoding_with_PASC.py --f example_sequences.txt"). This script will take in a text file (containing a peptide sequence(s)) and output their PASC feature encoded vector in csv format. "PASC_encoded_example_sequences.csv" is an example output file from "encoding_with_PASC.py", given the example_sequences.txt as input.

## If you are interested in accessing the PASC features used in our manuscript, we enclosed our data in the following folder:

/numpys; The enclosed files are the PASC features for the amino acids included in our manuscript, in numpy format. 


