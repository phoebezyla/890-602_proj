'''
A script to create job submission scripts for `aerie-apps-randomize-bkg`

Takes input .root files and creates one randomized.fits.gz file for each bin. Parameter/zenith alignment file and energy bins must be specified. Bins should be those that use randomized-background and NOT direct integration.

'''

import glob
import os
import sys
from math import ceil

aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
  # can source my aerie version, or your own! see aerie documentation on HAWC wiki to install
histLoc = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists"
  # where input histograms are located. same dir as output from make-histograms.py
combinedFiles="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/combined"
  # where input combined .fits.gz files are located. same dir as output from combine-raw-files.py
outputDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/randBkg"
  # where you want output randomized bkg .fits.gz files to go

zenithAlignmentFile = "$CONFIG_HAWC/reconstruction/alignment/align_pass5_v1.0/zenith-pass5-2021-08-13.xml"
  # parameter files should be in personal $CONFIG_HAWC if aerie installed and set up correctly
bins = ["B7C1","B8C0","B8C1","B9C0","B9C1","B10C0","B10C1"]
  # bins that require the randomize background estimation scheme. Only change if working with different binning scheme

for x in bins:  
  outfile = open("randomize-%s.sh"%(x), "w")
  outfile.write("#!/bin/sh\n#SBATCH --time=500\n#\n# INDIR:\n# __INDIR__\n# \n# RUN:\n# __RUN__")
  outfile.write("\n%s"%(aerie))
  outfile.write("\naerie-apps-randomize-bkg -o %s/bin%s-randomized.fits.gz -i %s/bin%s.root --zenith-alignment-file %s --useJ2000 --inputData %s/bin%s.fits.gz"%(outputDir, x, histLoc, x, zenithAlignmentFile,combinedFiles,x))
  outfile.close()
