#!/usr/bin/env python
import os
from ase.io import read, write
import sys

#files= os.listdir('.')
try:
    tar=sys.argv[1]
except IndexError:
    print "please give the name of the folder"
    exit()
    
os.system('cp init.traj  ' + str(tar))
os.system('vfin.pl '+str(tar))
if os.path.isfile('fin.traj'):
    os.system('cp  ' + str(tar) +'/fe.dat  .')
    os.system('rm init.traj')
else:
    ptmp=read('CONTCAR')
    pini=read(str(tar)+'/init.traj')
    mag=pini.get_initial_magnetic_moments()
    ptmp.set_initial_magnetic_moments(mag)
    write('init.traj', ptmp)

os.system('mv err* out* '+ str(tar))

