'''
A script to create job submission scripts for `aerie-apps-make-local-dists`

Takes input .txt files (which list .xcd files for each chunk) and creates one .root file for each bin for each chunk. Other input is a cut file. First part of creating randomized backgound for low-statistic energy bins. 
'''

chunkStart = 1 # first chunk you want to perform ana on
chunkEnd = 1511 # end chunk (of analysis) + 1

aerie = "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
  # can source my aerie version, or your own! see aerie documentation on HAWC wiki to install

cut = "/data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt" 
  # only need to make histograms for noDI bins
  # cut files also present in git repo -- rename these to where you copy in your directory
outDir = "/lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists/"
  # where you want histograms to be output

for x in range(chunkStart,chunkEnd):
  inFile = "`envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up/chunk00%04d.txt`"%(x)
    # need to be running on HAWC cluster for these to work. these .txt files point to data files too large to copy elsewhere
  outfile = open("hist-%04d.sh"%(x), "w")
  outfile.write("#!/bin/sh\n#SBATCH --time=30:00:00 --mem-per-cpu=8000mb\n#")
  outfile.write("\n%s"%(aerie))
  outfile.write("\naerie-apps-make-local-dists  --cuts %s --input %s -o %schunk%04d-bin%%s.root"%(cut,inFile,outDir,x))
  outfile.close()
