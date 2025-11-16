These are the scripts and fhit cut files to make fhit maps (including background estimation). The scripts assume that the chunks are already made, and the $CONFIG_HAWC is correctly set. 
Much of this repository has been modified from Kelly Malone's ground parameter map-making repository (https://gitlab.com/hawc-observatory/analysis-scripts/map-making/-/tree/master/counts-maps/GP-scripts?ref_type=heads).

# SCRIPT DESCRIPTIONS 
## `make-sub-scripts.py`
Creats job submission scripts for slurm to make the raw maps, broken into a reasonable number of jobs to reduce cluster memory usage. Need to specify aerie location, path to input .txt files, chunks to iterate over, parameter/zenith alignment file, cut file, and output directory. 
Note: There is one input text file for every chunk. Each text file has, on every line, the path to one .xcd file for that chunk. Each chunk has a different number of .xcd files.

## `combine-raw-files.py`
Creats job submission scripts to make one file for each bin, using `aerie-apps-combine-maps`. Specify the directory to the raw maps, a list of the energy bins to iterate over, aerie location, and output directory.

## `make-histograms.py`
Creates job submission scripts to begin the process of randomizing background for low-statistic bins. For the fhit energy estimator, this is for bins B7C1, B8C0, B8C1, B9C0, B9C1, B10C0, and B10C1. Specify aerie location, path to input .txt files, chunks to iterate over, cut file, and output directory.
Note: Chunks to iterate over needs to be the same as those used in `make-sub-scripts.py`. Otherwise the background randomization will fail because the histogram and map will have different numbers of evernts. 

## `make-randomized-bkg.py`
Creates job submission scripts to randomize the background for the bins with low statistics. Specify aerie location, location of histograms from `make-histograms.py`, location of combined files from `combine-raw-files.py`, list of bins to iterate over, parameter/zenith alignment file, and output directory.

# MAKING MAPS 
Direct Integration: B1C0-B7C0, B1C1-B6C1
	_allbins  B0C0 B0C1 B1C0 B1C1
	_2-10     B2-B5
	_bin6plus B6-B10
No Direct Integration: B8C0-B10C0, B7C1-B10C1
	_bin6plus B6-B10
