# Example Data (for testing)

Within this directory, you will find output files from each of the main map-making scripts. There is also a sub-directory with the slurm submission scripts for each process.

The output files here were created from the fHit 100% pass 5 machine learning cuts and data. These files are for chunks 2 and 3, and all bins. These files are meant to be run with `testing.sh`. It will show that the chunk 2 files are the same, but the combined files will be different

The files in both this test-data directory and those in the example directory do not represent the entire map-making process-- I have encountered a fully new error message when trying to combine histograms with `hadd` (see slurm output file). I've tried going through the root files themselves and cannot find what went wrong :( I will investigate further and try to fill out this directory will all steps in the workflow.

# Sub-directories

- `bash-scripts` contains the scripts used to create the files here
- `rejiggered` contains the final .fits.gz files that should be used when making significance plots