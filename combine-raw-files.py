'''
A script to create job submission scripts for `aerie-apps-combine-maps`

Creates one .fits.gz file for each bin. Input .fits.gz files are intended to be from `aerie-apps-make-hawc-maps`
'''

import glob
import os
import sys
from math import ceil

aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
  # can source my aerie version, or your own! see aerie documentation on HAWC wiki to install

inputDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/raw_100"
  # where the raw .fits.gz files are located. Same output as make-sub-scripts.py
outputDir="/lustre/hawcz01/scratch/userspace/zylaphoe/maps/combined"
  # where you want combined .fits.gz files to  be output

bins = ["B0C0","B0C1","B1C0","B1C1","B2C0","B2C1","B3C0","B3C1","B4C0","B4C1","B5C0","B5C1","B6C0","B6C1","B7C0","B7C1","B8C0","B8C1","B9C0","B9C1","B10C0","B10C1"]
  # bins to iterate over. Will be included in output file name 

for x in bins:
  outfile = open("combine-%s.sh"%(x), "w")
  outfile.write("#!/bin/sh\n#SBATCH --time=500\n#\n# INDIR:\n# __INDIR__\n#\n# RUN:\n# __RUN__")
  outfile.write("\n%s"%(aerie))
  outfile.write("\naerie-apps-combine-maps --inputs %s/*bin%s* -o %s/bin%s.fits.gz"%(inputDir,x,outputDir,x))
  outfile.close()
