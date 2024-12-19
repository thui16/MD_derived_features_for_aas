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

atom_types = ['H','C','N','O','S'] # All relevant atoms types
VdW_values = np.array([120,170,155,152,180])*0.01*1.88973 # VdW radii from pm to au
VdW = dict(zip(atom_types,VdW_values))

u_gro = mda.Universe('prot.gro')
u_tpr = mda.Universe('start0.tpr')
u_aligned = mda.Universe('aligned.xtc')

x_min,x_max,y_min,y_max,z_min,z_max = np.loadtxt('../global/size_data.txt') #read global voxel size

#refines the voxel size such that there is a spacing of 2.5A between each grid point for each direction
x_min = np.ceil(x_min)
x_max = np.floor(x_max)
while (int(x_max-x_min))%2.5 != 0:
    x_min -= 0.25
    x_max += 0.25

y_min = np.ceil(y_min)
y_max = np.floor(y_max)
while (int(y_max-y_min))%2.5 != 0:
    y_min -= 0.25
    y_max += 0.25

z_min = np.ceil(z_min)
z_max = np.floor(z_max)
while (int(z_max-z_min))%2.5 != 0:
    z_min -= 0.25
    z_max += 0.25

x_list = np.linspace(x_min,x_max,int((x_max-x_min)/2.5)+1)*1.88973
y_list = np.linspace(y_min,y_max,int((y_max-y_min)/2.5)+1)*1.88973
z_list = np.linspace(z_min,z_max,int((z_max-z_min)/2.5)+1)*1.88973
yy, xx, zz = np.meshgrid(y_list, x_list, z_list)
z = np.column_stack((xx.ravel(), yy.ravel(), zz.ravel())) # list of all grid points locations; shape is nubmer of grid points by 3

#for each frame in the trajectory, calculate the electrostatic potential
traj = u_aligned.trajectory
total_potential = np.zeros((len(z)))
for idx,i in enumerate(traj):
    positions = i.positions
    potential = np.zeros((len(z)))
    positions[:,[0,1,2]] = positions[:,[0,1,2]]
    for atom,position,charge in zip([i.type[0] for i in u_gro.atoms],positions*1.88973,u_tpr.atoms.charges):
        dists = np.sqrt(np.sum((z-position)**2,1))
        atom_potential = ((charge/dists)*erf(dists/(np.sqrt(2)*VdW[atom])))
        potential += atom_potential    
    total_potential += potential
total_potential = total_potential/len(traj) #takes the average potential over all frames
print(np.sum(np.isnan(total_potential)))
np.savetxt('sparse.txt', total_potential)
