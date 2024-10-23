#This code will read in the no_scaled backbone (BB) .npy features and perform the per_grid normalization

#Import python packages
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import numpy.ma as ma

#Define the function that will take in an four different arrays and output a per_grid normalized array. 
#The first array is the array that is to be normalized.
#The second array is the array where each grid point represents the minimum value of that grid point across a *specific set* of arrays.
#The third array is the array where each grid point represents the maximum value of that grid point across a *specific set* of arrays.
#The fourth array is the array where grid points are masked if there are any zero values
def min_max_normalize_global_wmask(arr,arr_min,arr_max,mask_array):
    arr=ma.masked_array(arr, mask=mask_array)

    new_X = (arr-arr_min)/(arr_max - arr_min)
    return new_X.data

#This is the list of amino acids we want to make normalized features for
AA_list=['ALA','Arg','Asn','Asp','Cys','Gln','Glu','GLY','His','Ile','Leu','Lys','Met','Phe','Ser','Thr',\
         'Trp','Tyr','Val','AIB','F4C','BFA','GML','HSE','NAL','PCF']

# This is the list of amino acids that will be in the *specific set*, i.e., the amino acids where the minimums and maximums are to be considered.
AA_list_15=['ALA','Arg','Asp','Asn','GLY','Phe','Ser','Val']

#The N values of N=[2,4,6,8,10,20,30,40,50,60,70,80,90,100]
bin_width_array_small=np.arange(2,10,2)
bin_width_array=np.arange(10,101,10)
bin_width_array=np.concatenate([bin_width_array_small,bin_width_array])

#Load the BB features for the *specific set* of amino acids and find the minimum grid points, maximum grid points, and the zero grid points.
for j in bin_width_array:
    num_of_bins=j
    AA_15_dict=dict()
    for AA in AA_list_15:
        file='../no_scale/numpys/'+str(num_of_bins)+'/'+AA+'_'+str(num_of_bins)+'_L_0530.npy'
        AA_name='L_'+AA
        AA_15_dict[AA_name]=np.load(file)

        file='../no_scale/numpys/'+str(num_of_bins)+'/'+AA+'_'+str(num_of_bins)+'_D_0530.npy'
        AA_name2='D_'+AA
        AA_15_dict[AA_name2]=np.load(file)
    
    combined_array=np.stack([AA_15_dict['L_ALA'],AA_15_dict['D_ALA'],AA_15_dict['L_Arg'],AA_15_dict['D_Arg'],\
                        AA_15_dict['L_Asp'],AA_15_dict['D_Asp'],AA_15_dict['L_Asn'],AA_15_dict['D_Asn'],\
                        AA_15_dict['L_GLY'],AA_15_dict['L_Phe'],AA_15_dict['D_Phe'],\
                        AA_15_dict['L_Ser'],AA_15_dict['D_Ser'],AA_15_dict['L_Val'],AA_15_dict['D_Val'],\
                        ])
    max_grid=np.max(combined_array,axis=0)
    min_grid=np.min(combined_array,axis=0)
    max_ind_zeros=np.where(max_grid == 0)
    mask_array = np.zeros([num_of_bins,num_of_bins], dtype=bool)
    for i in range(len(max_ind_zeros[0])):
        mask_array[max_ind_zeros[0][i]][max_ind_zeros[1][i]]=True
        
    #Load all of the amino acids we want to create normalized BB features for    
    AA_37_dict=dict()
    for AA in AA_list:
        file='../no_scale/numpys/'+str(num_of_bins)+'/'+AA+'_'+str(num_of_bins)+'_L_0530.npy'
        AA_name='L_'+AA
        AA_37_dict[AA_name]=np.load(file)

        file='../no_scale/numpys/'+str(num_of_bins)+'/'+AA+'_'+str(num_of_bins)+'_D_0530.npy'
        AA_name2='D_'+AA
        AA_37_dict[AA_name2]=np.load(file)
    
    for AA in AA_list:
        AA_name='L_'+AA
        L_arr=min_max_normalize_global_wmask(AA_37_dict[AA_name],min_grid,max_grid,mask_array)
        np.save('numpys/'+str(j)+'/'+AA+'_'+str(j)+'_L_0530_per_grid.npy',L_arr)

        AA_name='D_'+AA
        D_arr=min_max_normalize_global_wmask(AA_37_dict[AA_name],min_grid,max_grid,mask_array)
        np.save('numpys/'+str(j)+'/'+AA+'_'+str(j)+'_D_0530_per_grid.npy',D_arr)
        if np.max(L_arr.flatten()) or np.max(D_arr.flatten()):
            print(AA, np.max(L_arr.flatten()), np.max(D_arr.flatten()))
    
    print(j)
