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
    
os.system('vfin.pl '+str(tar))
os.system('mv init.traj  ' + str(tar))
os.system('mv err.* out.* '+ str(tar))
cwd=os.getcwd()
if os.path.isfile(cwd+'/fin.traj'):
    os.system('mv fin.traj init.traj')
else:
    ptmp=read('POSCAR')
    pini=read(str(tar)+'/init.traj')
    mag=pini.get_initial_magnetic_moments()
    ptmp.set_initial_magnetic_moments(mag)
    write('init.traj', ptmp)
