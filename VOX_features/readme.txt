# Getting started

This folder contains code and files related to our voxel features.

## If you want to generate your own voxel features using your own amino acid dipeptide MD simulations:

1. In the /AA folder, copy your trajectory .xtc and .tpr files. Run the Python script "align.py" (command is "python align.py"), which will align your trajectory to the "dummy.pdb" and output and aligned trajectory "aligned.xtc" and a "data.txt" file that lists the extreme values in the x,t, and z direction plus some buffer. This process is done in a new directory for each amino acid you want to include in your training dataset.

2. In the /global folder, run the Python script "get_size.py" (command is "python get_size.py"), which will collect all the "data.txt" files from each amino acid directory (like the example in /AA), find the global minima and maxima, and output a "size_data.txt" file that reports the size of the voxel that is large enough considering all the amino acids.

3. After obtaining the global extrema reported in "size_data.txt", go to the /AA folder and run the Python script "sparse_voxel.py" (command is "python sparse_voxel.py), which will calculate grid points with a 2.5A spacing to define the voxel,use the aligned.xtc to calculate the time-averaged molecular electrostatic potential, and output a "sparse.txt" file that lists the electrosatic potential at each grid point.

4. After getting a "sparse.txt" for each amino acid in your library, copy and rename each of the files (from "sparse.txt to "sparse_XXX.txt", where XXX is your amino acid three letter code) into a new directory called "all_voxel_feats". Then in the /global folder, run "final.py" (command is python final.py) which will read the files in "all_voxel_feats" and create a .json to store all the voxel features called "sparse_voxel.json". The file can be converted to numpy using the "make_numpys_from_json.py" python script

## If you want to encode peptide sequences:

1. Prepare a text file containing a peptide sequence(s). See "example_sequences.txt" as an example.

2. Run the python script encoding_with_VOX.py (example command: "python encoding_with_VOX.py --f example_sequences.txt"). This script will take in a text file (containing a peptide sequence(s)) and output their VOX feature encoded vector in csv format. "VOX_encoded_example_sequences.csv" is an example output file from encoding_with_VOX.py, given the example_sequences.txt as input.

## If you are interested in accessing the VOX features used in our manuscript, we enclosed our data in the following folder:

/numpys; The enclosed files are the VOX features for the amino acids included in our manuscript, in numpy format.





Analyze the backbone dihedral angles (phi, psi) from your MD simulation and prepare a .xvg (or .txt) file containing the simulation results (should have four columns, where the first column is the time, the second column is the average angle, the third column is the phi angle, and the fourth column is the psi angle).

2. Run the Python script "make_numpys_for_no_scale.py" (command is "python make_numpys_for_no_scale.py"). This code will bin the (phi,psi) distribution and create a .npy file for the BB feature (no normalization). NOTE: you will need to change the file name on line 14 of this script to match the file you prepared in step 1.

3. If you want to perform the "per grid" normalization as described in our manuscript, run the Python script "python make_numpys_for_bb_per_grid.py" (command is "python make_numpys_for_bb_per_grid.py"). This script will take the .npy files of the non-normalized features and perform the normalization.
