import glob
import os
import sys
from math import ceil

#anaDir= /lustre/hawcz01/scratch/userspace/zylaphoe/maps

histLoc = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists"

combinedFiles="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/combined"
outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/randBkg"

zenithAlignmentFile = "$CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml"
bins = ["B7C1","B8C0","B8C1","B9C0","B9C1","B10C0","B10C1"]

for x in bins:  
  outfile = open("randomize-%s.sh"%(x), "w")
  print >> outfile,"""#!/bin/sh
#SBATCH --time=500
#
# INDIR:
# __INDIR__
# 
# RUN:
# __RUN__

"""
  print >>outfile, "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
  print >>outfile,"aerie-apps-randomize-bkg -o %s/bin%s-randomized.fits.gz -i %s/bin%s.root --zenith-alignment-file %s --useJ2000 --inputData %s/bin%s.fits.gz"%(outputDir, x, histLoc, x, zenithAlignmentFile,combinedFiles,x)
  outfile.close()
