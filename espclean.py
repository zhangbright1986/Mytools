#!/usr/bin/env python

import os
import sys
from ase.io import read,write

try:
    tar=sys.argv[1]
except IndexError:
    print "please give the name of directory"
    exit()

if not os.path.isdir('./'+tar):
    os.system('mkdir '+tar)
else:
    print tar+' exist !!!'
    exit()

os.system('mv -f err* out* esp.log *node* '+tar)
os.system('cp init.traj fin.traj '+tar)
os.system('rm init.traj')

if not os.path.isfile('./fin.traj'):
    os.system('cp relax.traj init.traj')
    os.system('mv -f opt.log relax.traj ' +tar)
   
