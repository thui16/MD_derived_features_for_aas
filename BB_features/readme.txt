# Getting started

This folder contains code and files related to our backbone features.

## If you want to generate your own backbone features using your own amino acid dipeptide MD simulations:

1. Analyze the backbone dihedral angles (phi, psi) from your MD simulation and prepare a .xvg (or .txt) file containing the simulation results (should have four columns, where the first column is the time, the second column is the average angle, the third column is the phi angle, and the fourth column is the psi angle).

2. Run the Python script "make_numpys_for_no_scale.py" (command is "python make_numpys_for_no_scale.py"). This code will bin the (phi,psi) distribution and create a .npy file for the BB feature (no normalization). NOTE: you will need to change the file name on line 14 of this script to match the file you prepared in step 1.  

3. If you want to perform the "per grid" normalization as described in our manuscript, run the Python script "python make_numpys_for_bb_per_grid.py" (command is "python make_numpys_for_bb_per_grid.py"). This script will take the .npy files of the non-normalized features and perform the normalization.


## If you want to encode peptide sequences:

1. Prepare a text file containing a peptide sequence(s). See "example_sequences.txt" as an example.

2. Run the python script encoding_with_BB.py (example command: "python encoding_with_BB.py --f example_sequences.txt"). This script will take in a text file (containing a peptide sequence(s)) and output their BB feature encoded vector in csv format. "BB_encoded_example_sequences.csv" is an example output file from encoding_with_BB.py, given the example_sequences.txt as input.


## If you are interested in accessing the BB features used in our manuscript, we enclosed our data in the following folders:

Folder; description
============================
/numpys; The enclosed files are the backbone features for the amino acids included in our manuscript, in numpy format. They are the resulting 1D vectors after flattening the 40 by 40 grids that were used to bin the (phi,psi) distribution from the amino acid dipeptide molecular dynamics simulations. These features are "per-grid" normalized, as described in our manuscript, and were used to train the models shown in Figures 3,4, and 5 in the manuscript.

/for_plotting; The enclosed files are text files containing grid point coordinates of the 40 by 40 grids and their densities. These densities are the values used for the amino acid features (see the /numpys folder). These files were created to easily visualize the (phi,psi) distributions and can be plotted with any software of your choice. These features are "per-grid" normalized, as described in our manuscript.

/numpys_no_normalization; The enclosed files are the backbone features for the amino acids included in our manuscript, in numpy format. They are the resulting 1D vectors after flattening the 40 by 40 grids that were used to bin the (phi,psi) distribution from the amino acid dipeptide molecular dynamics simulations. These features are not normalized, and were not used to train the models shown in Figures 3,4, and 5 in the manuscript. They are provided just to show what the "raw" feature looks like before our applied normalization.

/for_plotting_no_normalization; The enclosed files are text files containing grid point coordinates of the 40 by 40 grids and their densities. These densities are the values used for the amino acid features (see the /numpys folder). These files were created to easily visualize the (phi,psi) distributions and can be plotted with any software of your choice. These features are not normalized, and were not used to train the models shown in Figures 3,4, and 5 in the manuscript. They are provided just to show what the "raw" feature looks like before our applied normalization.
