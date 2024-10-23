Folder or file; description
============================
/numpys; The enclosed files are the backbone features for the amino acids included in our manuscript, in numpy format. They are the resulting 1D vectors after flattening the 40 by 40 grids that were used to bin the (phi,psi) distribution from the amino acid dipeptide molecular dynamics simulations. These features are "per-grid" normalized, as described in our manuscript, and were used to train the models shown in Figures 3,4, and 5 in the manuscript.

/for_plotting; The enclosed files are text files containing grid point coordinates of the 40 by 40 grids and their densities. These densities are the values used for the amino acid features (see the /numpys folder). These files were created to easily visualize the (phi,psi) distributions and can be plotted with any software of your choice. These features are "per-grid" normalized, as described in our manuscript.

encoding_with_BB.py; An example python script that will take in a text file (containing a peptide sequence(s)) and output their BB feature encoded vector in csv format. Example command: 'python encoding_with_BB.py --f example_sequences.txt' 

example_sequences.txt; An example text file that will be input into encoding_with_BB.py

BB_encoded_example_sequences.csv; An example output file from encoding_with_BB.py, given the example_sequences.txt as input.

make_numpys_for_no_scale.py; A python script that will take dihedral .xvg (or .txt) files from the dipeptide simulation results (should have four columns, where the first column is the time, the second column is the average angle, the third column is the phi angle, and the fourth column is the psi angle), bin the (phi,psi) distribution, and create the .npy for the BB feature (no normalization).

make_numpys_for_bb_per_grid.py; A python script that will take the .npy files in the /numpys_no_normalization folder and perform the normalization.

/numpys_no_normalization; The enclosed files are the backbone features for the amino acids included in our manuscript, in numpy format. They are the resulting 1D vectors after flattening the 40 by 40 grids that were used to bin the (phi,psi) distribution from the amino acid dipeptide molecular dynamics simulations. These features are not normalized, and were not used to train the models shown in Figures 3,4, and 5 in the manuscript. They are provided just to show what the "raw" feature looks like before our applied normalization.


/for_plotting_no_normalization; The enclosed files are text files containing grid point coordinates of the 40 by 40 grids and their densities. These densities are the values used for the amino acid features (see the /numpys folder). These files were created to easily visualize the (phi,psi) distributions and can be plotted with any software of your choice. These features are not normalized, and were not used to train the models shown in Figures 3,4, and 5 in the manuscript. They are provided just to show what the "raw" feature looks like before our applied normalization.
