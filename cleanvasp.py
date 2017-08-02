#!/usr/bin/env python
import os
from ase.io import read, write
from ase.calculators.vasp import Vasp
import sys

calc = Vasp(restart=True)
p= calc.get_atoms()
write('fin.traj',p)

try:
    tar=sys.argv[1]
except IndexError:
    print "please give the name of the folder"
    exit()
    
os.system('vfin.pl '+str(tar))
os.system('cp init.traj fin.traj ' + str(tar))

if os.path.isfile('fin.traj'):
    os.system('cp  ' + str(tar) +'/fe.dat  .')
    os.system('rm init.traj')
else:
    ptmp=read(str(tar)+'/CONTCAR')
    pini=read(str(tar)+'/init.traj')
    mag=pini.get_initial_magnetic_moments()
    ptmp.set_initial_magnetic_moments(mag)
    write('init.traj', ptmp)

os.system('mv err* out* '+ str(tar))

