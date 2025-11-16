'''
A script to create job submission scripts for `aerie-apps-make-hawc-maps`

Takes input .txt files (which list .xcd files for each chunk) and creates one ,fits.gz file for each bin for each chunk. Cuts file, parameter file, and input .txt files must be changed depending on the working bin group, and whether it uses DI or randBkg for its background estimator. 

'''
import glob
import os
import sys
from math import ceil

outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/raw_100"
aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"

chunkStart = 1 #first chunk to include
chunkEnd = 1511 #last chunk to include + 1 
groupNames = ['01','25','67','710']

cuts_01="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_0-1.txt" #Bins 0-1, DI 
cuts_25="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_2-5.txt" #Bins 2-5, DI
cuts_67="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_6-7.txt" #Bins 6-7, DI
cuts_710="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt" #Bins 7-10, noDI 
cuts_arr = [cuts_01, cuts_25, cuts_67, cuts_710]

paramsDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 1.2 --dtMax_hr 2.0 --nSide 1024 --roi --useJ2000 --rndSmear'
paramsNoDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 0 --dtMax_hr 2.0 --nSide 1024 --useJ2000 --rndSmear'
param_arr = [paramsDI, paramsDI, paramsDI, paramsNoDI]

path01  = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_allbin/chunk%06d.txt`"%(x) #Bins 0-1, DI
path25  = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin2up/chunk%06d.txt`"%(x) #Bins 2-5, DI
path610 = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up/chunk%06d.txt`"%(x) #Bins 6-10, DI and noDI
path_arr = [path01, path25, path610, path610]    

for x in range (chunkStart,chunkEnd): # iterate over chunks
    for i in range(4):# iterate over bin groups
        file_name = "ch%04d-%s.sh"%(x,groupNames[i]
        outfile = open(file_name, "w") #CHANGE W CUT FILE
        print("""#!/bin/sh
#SBATCH --time=30:00:00 --mem-per-cpu=8000mb
#
# INDIR:
# __INDIR__
# 
# RUN:
# __RUN__

""",file=outfile)
        print("%s"%(aerie),file=outfile)
        print("which offline-reconstructor" ,file=outfile)
        print("aerie-apps-make-hawc-maps --input %s -p %s -n ch%04d --cutFile %s %s"%(path_arr[i],outputDir,x,cuts_arr[i],param_arr[i]),file=outfile)
        outfile.close()

