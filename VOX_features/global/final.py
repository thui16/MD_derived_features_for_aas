#%%

import os
import numpy as np
import json
from sklearn.decomposition import PCA

#%%

directory = '../all_voxel_feats/'
files = os.listdir(directory)

sparse_aa_list = []
sparse_voxel = []
for file in files:
    if file.split('.')[1] == 'txt':
        if file.split('_')[0] == 'sparse':
            if file.split('_')[1].split('.')[0] == 'Gly' or file.split('_')[1].split('.')[0] == 'AIB':
                sparse_voxel.append((np.loadtxt(directory+file)+np.loadtxt(directory+file).reshape(11,11,13)[:,:,::-1].reshape(11*11*13))*0.5)
                sparse_aa_list.append('L-'+file.split('_')[1].split('.')[0])
            else:
                sparse_voxel.append(np.loadtxt(directory+file))
                sparse_aa_list.append('L-'+file.split('_')[1].split('.')[0])
                sparse_voxel.append(np.loadtxt(directory+file).reshape(11,11,13)[:,:,::-1].reshape(11*11*13))
                sparse_aa_list.append('D-'+file.split('_')[1].split('.')[0])
print(sparse_aa_list)

data_sparse_list = [list(np.array(i,dtype=float)) for i in sparse_voxel]
dict_sparse = dict(zip(sparse_aa_list,data_sparse_list))
json_data = json.dumps(dict_sparse)
with open(f"sparse_voxel.json", "w") as json_file:
    json_file.write(json_data)

