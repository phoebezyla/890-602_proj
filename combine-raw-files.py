import glob
import os
import sys
from math import ceil

anaDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps"
inputDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/raw_100"
outputDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/combined"
i=1
bins = ["B0C0","B0C1","B1C0","B1C1","B2C0","B2C1","B3C0","B3C1","B4C0","B4C1","B5C0","B5C1","B6C0","B6C1","B7C0","B7C1","B8C0","B8C1","B9C0","B9C1","B10C0","B10C1"]
for x in bins:
  outfile = open("combine-%s.sh"%(x), "w")
  print >> outfile,"""#!/bin/sh
#SBATCH --time=500
#
# INDIR:
# __INDIR__
# 
# RUN:
# __RUN__
"""
  #print >> outfile,"cd %s"%(outputDir)
  print >> outfile,"mkdir -p combined"
  print >>outfile,"aerie-apps-combine-maps --inputs %s/*bin%s* -o %s/bin%s.fits.gz"%(inputDir,x,outputDir,x)
  outfile.close()
