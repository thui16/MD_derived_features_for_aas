Folder or file; description
============================
/numpys; The enclosed files are the voxel features for the amino acids included in our manuscript, in numpy format. They are the resulting 1D vectors after flattening the 11 by 11 by 13 voxel that represented the molecular electrostic potentials from the amino acid dipeptide molecular dynamics simulations.These features are not normalized.

encoding_with_VOX.py; An example python script that will take in a text file (containing a peptide sequence(s)) and output their VOX feature encoded vector in csv format. Example command: 'python encoding_with_VOX.py --f example_sequences.txt' 

example_sequences.txt; An example text file that will be input into encoding_with_VOX.py

VOX_encoded_example_sequences.csv; An example output file from encoding_with_VOX.py, given the example_sequences.txt as input.
