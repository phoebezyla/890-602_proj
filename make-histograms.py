import glob
import os
import sys
from math import ceil

homeDir="/data/disk01/home/zylaphoe/maps-making-ML"
anaDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps"

dezhiDir="/lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/"

#3 input/output directories: first is all bins, second is bins 2up, third is bin 6 up
inputDir="/lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up"  #only randomized bkg are B7C1-> and B8C0->

outputDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists"

cutsFile = "/data/disk01/home/zylaphoe/maps-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt"

i=1
for x in range (1,1511):
  outfile = open("hist-%04d.sh"%(x), "w")
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
  print >>outfile, "aerie-apps-make-local-dists --input `envsubst < %s/chunk%06d.txt` --cuts %s -o chunk%04d-bin%%s.root"%(inputDir,x,cutsFile,x)
  outfile.close()
