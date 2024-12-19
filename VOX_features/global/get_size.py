### RUN SECOND ###

import os
import numpy as np

sizes = []
#os.chdir('../')
#path = os.getcwd()
#items = os.listdir(path)
items=['ALA','Arg','Asp','Asn','GLY','Phe','Ser','Val'] #list of ammino acid directoriess
for item in items:
    if item != 'global':
        sizes.append(np.loadtxt(f'../{item}/data.txt'))
        print(np.loadtxt(f'../{item}/data.txt'))

sizes = np.array(sizes)
# find the global minima and maxima in each direction to determine the size of the voxel
full_box = np.array([np.min(sizes[:,0]),np.max(sizes[:,1]),np.min(sizes[:,2]),np.max(sizes[:,3]),np.min(sizes[:,4]),np.max(sizes[:,5])])
np.savetxt('size_data.txt',full_box)



