#!/bin/bash/ --login
#SBATCH --mem=2000gb
#SBATCH --time=10:00:00

for x in range (40,1511):
  outfile = open("hist-%04d.sh"%(x), "w")
  print >> outfile,"""#!/bin/sh
#SBATCH --time=30:00:00 --mem-per-cpu=8000mb
#
"""
  print >>outfile, "source /data/disk01/home/zylaphoe/hawc_software/init_aerie.sh"
  print >>outfile, "cd /lustre/hawcz01/scratch/userspace/zylaphoe/maps/hists/"
  print >>outfile, "aerie-apps-make-local-dists  --cuts /data/disk01/home/zylaphoe/map-making-ML/fNhit_100pct_pgamma_mlp_cut_7up_noDI.txt --input `envsubst < /lustre/hawcz01/scratch/userspace/dezhih/service/nn_estimator/nn_sky_map/chunk_map/pass5-chunk-1000-1090-ML/pass5_bin6up/chunk00%04d.txt` -o chunk%04d-bin%%s.root"%(x,x)

  outfile.close()
