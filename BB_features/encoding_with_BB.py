# This example code will take in a example_sequences.txt file,
# encode the sequences using the BB features (store in .npy format),
# and output an BB_encoded_example_sequences.csv

# example command 'python encoding_with_BB.py --f example_sequences.txt'

import sys
import numpy as np
import pandas as pd
from argparse import ArgumentParser

# function used to split a peptide sequence into amino acid components
def splitby_char(word):
    return [char for char in word]


# read in the a example_sequences.txt file or throw an error
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
args = parser.parse_args()

if args.filename == None:
	print('please provide a valid file')
	sys.exit()

else: 
	with open(args.filename) as f:
		sequences=f.read().splitlines() 
	f.close()


# A list of the amino acid 1-letter and 3-letter codes. 
# Note that we chose letters to the non-canonical amino acids 
# that were not already assigned to the canonical amino acids. 
# Because we ran out of the 26 letters in the alphabet, and because AIB is achiral, we assigned it a number "1".
one_lett_code=['A','R','N','D','C','Q','E','G','H','I','L','K',\
'M','F','S','T','W','Y','V','J','1','B','O','Z','X','U']
three_lett_code=['ALA','Arg','Asn','Asp','Cys','Gln','Glu','GLY','His','Ile','Leu','Lys',\
'Met','Phe','Ser','Thr','Trp','Tyr','Val','GML','AIB','BFA','NAL','F4C','PCF','HSE']

# Assign each of the amino acids their feature value from the numpy file using a dictionary
# (the uppercase letters denote the L-form and the lowercase letters denote the D-form)
AA_dict=dict()
for i in range(len(three_lett_code)):
    l_aa_array=np.load('numpys/'+str(three_lett_code[i])+'_40_L_0530_per_grid.npy')
    d_aa_array=np.load('numpys/'+str(three_lett_code[i])+'_40_D_0530_per_grid.npy')
    AA_dict[one_lett_code[i]]=l_aa_array.flatten()
    AA_dict[one_lett_code[i].lower()]=d_aa_array.flatten()

# encode the sequences
seq_dict=dict()
for seq in sequences:
    encodings=[]
    aas=splitby_char(seq)
    for i in aas:
        encodings.append(AA_dict[i])
    seq_dict[seq]=encodings

#Code to make the array of arrays just one array. 
for seq in seq_dict:    
    seq_dict[seq]=[item for sublist in seq_dict[seq] for item in list(sublist)]
sequences_for_NN=list(seq_dict.keys())

#Store the values as the X array.
X=np.array(list(seq_dict.values()),dtype=object)

dataframe_X = pd.DataFrame(X)
dataframe_X.index = sequences
filename_no_extension=args.filename.split('.')[0]
dataframe_X.to_csv('BB_encoded_'+str(filename_no_extension)+'.csv')




