import numpy as np
import json

f = open('sparse_voxel.json')
voxel_pcs = json.load(f)
f.close()

for AA in list(voxel_pcs.keys()):
    tmp_file_name='1573/'+AA[-3:]+'_1573_'+AA[0]+'_0530.npy'
    np.save(tmp_file_name,voxel_pcs[AA])

