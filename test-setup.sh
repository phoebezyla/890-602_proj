#!/bin/bash 


# To test correctly, need to be in base conda environment
# If your aerie is named something different, please change aerie variable
aerie="aerie_env"

# check if slurm available (commands on PATH)
if command -v srun >/dev/null 2>&1; then
	echo "Slurm is available"
	HAS_SLURM=1
else 
	echo "Slurm is NOT available"
	HAS_SLURM=0
fi 

# check if AERIE available and installed correctly 
if ! command -v conda >/dev/null 2>&1; then
	echo "Conda is not available"
	exit 1
fi 

# need to source conda before able to use conda commands 
source "$(conda info --base)/etc/profile.d/conda.sh" 

if conda env list | awk '{print $2}' | grep -q "$aerie"; then
	echo "Conda env '$aerie' available"
	HAS_ENV=1
else
	echo "Conda env '$aerie' NOT available :("
	HAS_ENV=0
fi

if [ "$HAS_SLURM" -eq 1 ] && [ "$HAS_ENV" -eq 1 ]; then
	echo "Ready to submit job to slurm w AERIE environment"
fi
