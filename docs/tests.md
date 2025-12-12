# Tests

The AERIE functions within each .py script (`aerie-apps-combine-maps`, `aerie-apps-make-local-dists`, `aerie-apps-randomize-bkg`, and `aerie-apps-make-hawc-maps`) are tested by the AERIE developers before being published. If interested in the tests/AERIE development, please reach out to the following slack channels: # softwareworkshop, # software-help, or # analysis-chat. 


To test your own I/O process, please interactively run `testing.sh`. It will check whether your produced files match the produced example files in the `example` folder. You will need to make sure that `testing.sh` points to your produced files. To test the availability of SLURM and AERIE environment, please run `test-setup.sh`. If you have a different name for your AERIE environment than `aerie_env`, please change that variable in the testing script. 

NOTE: HAWC's data is not ready for public relesae, so only the files created by the .py scripts are available in this repository. For the purpose of proving that these tests work (for CMSE proj), I have run the process twice on different chunks of data. Two chunks (1, 2) were output to the `example` folder (for others to check against) and two chunks (2, 3) to the `test-data` folder (to show for class that `testing.py` works / can tell that these were created with different chunks)