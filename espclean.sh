#!/bin/sh

tar=$1
mkdir $tar
cp init.traj  relax.traj $tar
mv relax.traj init.traj
mv opt.log err* out* esp.log *node* $tar
