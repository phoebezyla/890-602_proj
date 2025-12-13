# Example Data (for testing)
Example files were way too big for github! Basic structure for tests is available here. 

Within this directory, you will find output files from each of the main map-making scripts. There is also a sub-directory with the slurm submission scripts for each process.

The output files here were created from the fHit 100% pass 5 machine learning cuts and data. These files are for chunks 1 and 2, and all bins.

The files in both this example directory and those in the test-data directory do not represent the entire map-making process-- I have encountered a fully new error message when trying to combine histograms with `hadd` (see slurm output file). I've tried going through the root files themselves and cannot find what went wrong :( I will investigate further and try to fill out this directory will all steps in the workflow.
# Sub-directories

- `bash-scripts` contains the scripts used to create the files here
- `rejiggered` contains the final .fits.gz files that should be used when making significance plots