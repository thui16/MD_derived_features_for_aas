#This code will read in the dihedral .xvg (or .txt) files and output the backbone (BB) features (no normalization) in .npy file format for all N by N grids (where N=[2,4,6,8,10,20,30,40,50,60,70,80,90,100]) .

#Import python packages
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd


#Read the files in the folder that contains the .xvg (or .txt) files. 
#In our case, the .txt files are named 'XXX_both.txt' (where XXX is the amino acid three letter code) 

file_list=[]
for name in glob.glob('*_both.txt'):
    file_list.append(name)


#We will create the array of N values 
bin_width_array_small=np.arange(2,10,2)
bin_width_array=np.arange(10,101,10)
bin_width_array=np.concatenate([bin_width_array_small,bin_width_array])

#The loop that will calculate the BB feature for each N value
for val in bin_width_array:
    num_of_bins=val
    bin_width=360/num_of_bins #the bin width is 360 degrees divided by the number of bins 

    for file in file_list:
        file_AA_name=file.split('_')[0] #this split depends on the file list and file name, as we just want to isolate the AA name based on the MD data in the .txt files. Adjust as needed based on you file naming scheme
        if file_AA_name not in ['GLY','AIB']: #just checking if the 'XXX_both.txt' file is for an achiral amino acid like GLY or AIB. 
	        with open(file) as f:
	            lines=f.readlines()
	            phi_all=[]
	            psi_all=[]
	            for k,line in enumerate(lines): #each line is in the format of time, average angle, phi angle, psi angle.
	                splits=line.split()
	                phi_all.append(float(splits[2]))
	                psi_all.append(float(splits[3]))

	            custom_bins=np.arange(-180,181,bin_width)
	            f2 = plt.figure(figsize=(10,3))
	            ax = f2.add_subplot(121)
	            ax2 = f2.add_subplot(122)

                #Bin the phi and psi angles with a 2D histogram 
	            h_all, xedges_all, yedges_all, image=ax2.hist2d(phi_all,psi_all, bins=custom_bins,density=False)
	            x_centers_all=[0]*num_of_bins
	            y_centers_all=[0]*num_of_bins
	            prob_density_all=(h_all/np.sum(h_all))/(bin_width**2)

	            #Convert to the transpose for easier plotting and the correct centrosymmetric transformation for the D-form of the amino acid. 
	            prob_density_all_L=np.transpose(prob_density_all)[::-1]
	            prob_density_all_D=np.transpose(prob_density_all[::-1])

                #Save the .npy files 
	            np.save('numpys/'+str(num_of_bins)+'/'+str(file_AA_name)+'_'+str(num_of_bins)+'_L_0530.npy', prob_density_all_L)
	            np.save('numpys/'+str(num_of_bins)+'/'+str(file_AA_name)+'_'+str(num_of_bins)+'_D_0530.npy', prob_density_all_D)

	            print('done with'+str(file_AA_name)+'_'+str(num_of_bins))


        if file_AA_name in ['GLY','AIB']: #If the amino acid is achiral, then we will symmetrize the (phi,psi) distribution such that the centrosymmetric points are averaged. 
	        with open(file) as f:
	            lines=f.readlines()
	            phi_all=[]
	            psi_all=[]
	            for k,line in enumerate(lines): #each line is in the format of time, average angle, phi angle, psi angle.
	                splits=line.split()
	                phi_all.append(float(splits[2]))
	                psi_all.append(float(splits[3]))

	            custom_bins=np.arange(-180,181,bin_width)
	            f2 = plt.figure(figsize=(10,3))
	            ax = f2.add_subplot(121)
	            ax2 = f2.add_subplot(122)

                #Bin the phi and psi angles with a 2D histogram
	            h_all, xedges_all, yedges_all, image=ax2.hist2d(phi_all,psi_all, bins=custom_bins,density=False)
	            x_centers_all=[0]*num_of_bins
	            y_centers_all=[0]*num_of_bins

	            prob_density_all=(h_all/np.sum(h_all))/(bin_width**2)
                #Convert to the transpose for easier plotting
	            prob_density_all_L=np.transpose(prob_density_all)[::-1]
                
                #Symmetrize the (phi,psi) distribution of the achiral amino acid by taking the average of the appropriate centrosymmetric pairs.
                #First, split the (phi,psi) distribution in the 2D grid based on a top and bottom half.
	            top_half=prob_density_all_L[0:int(len(prob_density_all_L)/2)]
	            bottom_half=prob_density_all_L[int(len(prob_density_all_L)/2):]
                
                #Reverse the bottom half such that the value that was originally in the last column is now in the first column
	            bottom_half_rev=[]
	            for row in bottom_half:
	               bottom_half_rev.append(row[::-1])
	            bottom_half_rev=np.array(bottom_half_rev)

                #Mirror the bottom half such that the calues that were originally in the last row are now in the first row
	            bottom_half_rev_mirror=bottom_half_rev[::-1]

                #Take the average of the two centrosymmteric values
	            top_half_avg=np.array((top_half+bottom_half_rev_mirror)/2)    

                #'Undo' the transformations done onto the the bottom half of the 2D grid but keeping the avergaed values
	            bottom_half_avg_rev_mirror=top_half_avg[::-1]
	            bottom_half_avg_rev=[]
	            for row in bottom_half_avg_rev_mirror:
	               bottom_half_avg_rev.append(row[::-1])
	            bottom_half_avg_rev=np.array(bottom_half_avg_rev)
	            prob_density_all_L=np.vstack([top_half_avg,bottom_half_avg_rev])

                #Since these amino acids are achiral, there is no L- or D- form. 
                #However, for consistent naming and reading during the encoding process, we will have a "L" numpy and "D" numpy for the achiral amino acid, but these numpys are identical. 
                #(e.g., if you diff ALA_100_D_0530.npy ALA_100_L_0530.npy, they will differ. But if you diff AIB_100_D_0530.npy AIB_100_L_0530.npy, they will be the same). 
	            np.save('numpys/'+str(num_of_bins)+'/'+str(file_AA_name)+'_'+str(num_of_bins)+'_L_0530.npy', prob_density_all_L)
	            np.save('numpys/'+str(num_of_bins)+'/'+str(file_AA_name)+'_'+str(num_of_bins)+'_D_0530.npy', np.flip(prob_density_all_L))
	            print('done with'+str(file_AA_name)+'_'+str(num_of_bins))

