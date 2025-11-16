import glob
import os
import sys
from math import ceil

outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/raw_100"
aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
i=1

#cuts="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_0-1.txt" #Bins 0-1, DI 
#cuts="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_2-5.txt" #Bins 2-5, DI
cuts="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_6-7.txt" #Bins 6-7, DI
#cuts="/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt" #Bins 7-10, noDI 

paramsDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 1.2 --dtMax_hr 2.0 --nSide 1024 --roi --useJ2000 --rndSmear'
paramsNoDI = '-z $CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml --dtMin 0 --dtMax_hr 2.0 --nSide 1024 --useJ2000 --rndSmear'

#EDIT THE NEXT TWO LINES WITH THE CHUNKS YOU WANT TO USE TO MAKE MAPS


for x in range (1,1511):
    #path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_allbin/chunk%06d.txt`"%(x) #Bins 0-1, DI
    #path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin2up/chunk%06d.txt`"%(x) #Bins 2-5, DI
    path = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up/chunk%06d.txt`"%(x) #Bins 6-10, DI and noDi
    
    #if os.path.isdir(path):
        #for y in range (1, 4): 
    outfile = open("ch%04d-DI-6up.sh"%(x,), "w") #CHANGE W CUT FILE
    i=i+1
    print >> outfile,"""#!/bin/sh
#SBATCH --time=30:00:00 --mem-per-cpu=8000mb
#
# INDIR:
# __INDIR__
# 
# RUN:
# __RUN__

"""
    print >>outfile, "%s"%(aerie)
    print >>outfile, "which offline-reconstructor" 
    print >>outfile, "aerie-apps-make-hawc-maps --input %s -p %s -n ch%04d --cutFile %s %s"%(path,outputDir,x,cuts,paramsNoDI)
    outfile.close()

    #for y in range (1, 2):
    #    outfile = open("ch%04d-nonDI-%d-pass5-fHit-2pct-ML.sh"%(x,y), "w")
    #    i=i+1
    #    print >>outfile,"""#!/bin/sh
#SBATCH --time=168:00:00 --mem-per-cpu=8000mb
#
# INDIR:
# __INDIR__
# 
# RUN:
# __RUN__

#"""
    #    print >>outfile, "%s"%(aerie)
    #    print >>outfile, "which offline-reconstructor"
    #    print >>outfile, "aerie-apps-make-hawc-maps --input %s -p %s -n ch%04d --cutFile %s/cuts-nonDI-%d.txt %s"%(path,outputDir,x,cutsDir,y,paramsNoDI)

    #    outfile.close()

