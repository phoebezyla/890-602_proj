'''
A script to create job submission scripts for `aerie-apps-make-hawc-maps`

Takes input .txt files (which list .xcd files for each chunk) and creates one .fits.gz file for each bin for each chunk. Cuts file, parameter file, and input .txt files must be changed depending on the working bin group, and whether it uses DI or randBkg for its background estimator. 

'''
import glob
import os
import sys
from math import ceil

outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/raw_100"
    # choose where you want raw .fits.gz files to be output
aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
    # can source my aerie version, or your own! see aerie documentation on HAWC wiki to install

chunkStart = 1 #first chunk to include
chunkEnd = 1511 #last chunk to include + 1 
groupNames = ['B0-1','B2-5','B6-7','B7-10-noDI'] # bin group names -- to be appended to output file name

cuts_01="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_0-1.txt" #Bins 0-1, DI 
cuts_25="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_2-5.txt" #Bins 2-5, DI
cuts_67="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_6-7.txt" #Bins 6-7, DI
cuts_710="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt" #Bins 7-10, noDI 
    # cut files also present in git repo -- rename these to where you copy in your directory
cuts_arr = [cuts_01, cuts_25, cuts_67, cuts_710]

paramsDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 1.2 --dtMax_hr 2.0 --nSide 1024 --roi --useJ2000 --rndSmear'
paramsNoDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 0 --dtMax_hr 2.0 --nSide 1024 --useJ2000 --rndSmear'
    # parameter files should be in personal $CONFIG_HAWC if aerie installed and set up correctly
param_arr = [paramsDI, paramsDI, paramsDI, paramsNoDI]

for x in range (chunkStart,chunkEnd): # iterate over chunks
    for i in range(4):# iterate over bin groups
        # define path to .txt files based on bin group
        if i == 0:
            path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_allbin/chunk%06d.txt`"%(x) #Bins 0-1, DI
        elif i ==1:
            path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin2up/chunk%06d.txt`"%(x) #Bins 2-5, DI
        else:
            path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up/chunk%06d.txt`"%(x) #Bins 6-10, DI and noDI
        # need to be running on HAWC cluster for these to work. these .txt files point to data files too large to copy elsewhere
        
        file_name = "ch%04d-%s.sh"%(x,groupNames[i])

        outfile = open(file_name, "w") #CHANGE W CUT FILE
        outfile.write("#!/bin/sh\n#SBATCH --time=30:00:00 --mem-per-cpu=8000mb\n#\n#INDIR:\n#__INDIR__ \n#\n#RUN\n#__RUN__")
        outfile.write("\n%s"%(aerie))
        outfile.write("\nwhich offline-reconstructor")
        outfile.write("\naerie-apps-make-hawc-maps --input %s -p %s -n ch%04d_%s --cutFile %s %s"%(path,outputDir,x,groupNames[i],cuts_arr[i],param_arr[i]))
        outfile.close()

