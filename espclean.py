#!/usr/bin/env python

import os
import sys
from ase.io import read,write


tar=sys.argv[1]

if not os.path.isdir('./'+tar):
    os.system('mkdir '+tar)
else:
    print tar+' exist !!!'
    exit()

os.system('mv opt.log err* out* esp.log *node* relax.traj'+tar)
os.system('cp init.traj fin.traj '+tar)
os.system('rm init.traj')

if not os.path.isfile('./fin.traj'):
    os.system('cp '+tar+'/relax.traj init.traj')
