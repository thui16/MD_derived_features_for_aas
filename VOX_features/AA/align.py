#%%### --- LOAD MODULES --- ###

print('load modules')

import numpy as np
import os
from scipy.special import erf
import MDAnalysis as mda
from MDAnalysis.analysis import align
import matplotlib.pyplot as plt

#%%

print('align traj')

u_pdb = mda.Universe('dummy.pdb') #template of reference to align trajectory frames to
u_xtc = mda.Universe('prot.gro','s1s2_all.xtc') #trajectory 
u_tpr = mda.Universe('start0.tpr') #trajectory tpr
align.AlignTraj(u_xtc, u_pdb, select='resid 2 and (name N or name CA or name C)', filename='aligned.xtc').run()
u_aligned = mda.Universe('aligned.xtc')

#%%

print('get xyz max')


ll = 5 #buffer 
traj = u_aligned.trajectory
x_max,x_min,y_max,y_min,z_max,z_min = 0,0,0,0,0,0

#find the furthest coordinates in the x,y,z directions
for idx,i in enumerate(traj):
    if x_max < np.max(i.positions[:,0]): x_max = np.max(i.positions[:,0])
    if x_min > np.min(i.positions[:,0]): x_min = np.min(i.positions[:,0])
    if y_max < np.max(i.positions[:,1]): y_max = np.max(i.positions[:,1])
    if y_min > np.min(i.positions[:,1]): y_min = np.min(i.positions[:,1])
    if z_max < np.max(i.positions[:,2]): z_max = np.max(i.positions[:,2])
    if z_min > np.min(i.positions[:,2]): z_min = np.min(i.positions[:,2])

#add the buffer room to the coordinates
x_max,x_min,y_max,y_min,z_max,z_min = x_max+ll,x_min-ll,y_max+ll,y_min-ll,z_max+ll,z_min-ll
if -1*z_max < z_min: z_min = -1*z_max
if -1*z_min > z_max: z_max = -1*z_min
data = np.array([x_min,x_max,y_min,y_max,z_min,z_max])
np.savetxt('data.txt', data)



