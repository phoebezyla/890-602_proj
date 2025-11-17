'''
A script to create job submission scripts for `aerie-apps-randomize-bkg`

Takes input .root files and creates one randomized.fits.gz file for each bin. Parameter/zenith alignment file and energy bins must be specified. Bins should be those that use randomized-background and NOT direct integration.

'''

import glob
import os
import sys
from math import ceil

aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"

histLoc = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists"
combinedFiles="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/combined"
outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/randBkg"

zenithAlignmentFile = "$CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml"
bins = ["B7C1","B8C0","B8C1","B9C0","B9C1","B10C0","B10C1"]

for x in bins:  
  outfile = open("randomize-%s.sh"%(x), "w")
  outfile.write("#!/bin/sh\n#SBATCH --time=500\n#\n# INDIR:\n# __INDIR__\n# \n# RUN:\n# __RUN__")
  outfile.write("\n%s"%(aerie))
  outfile.write("\naerie-apps-randomize-bkg -o %s/bin%s-randomized.fits.gz -i %s/bin%s.root --zenith-alignment-file %s --useJ2000 --inputData %s/bin%s.fits.gz"%(outputDir, x, histLoc, x, zenithAlignmentFile,combinedFiles,x))
  outfile.close()
