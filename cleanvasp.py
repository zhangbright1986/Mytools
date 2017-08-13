#!/usr/bin/env python
import os
from ase.io import read, write
from ase.calculators.vasp import Vasp
import sys


try:
    tar=sys.argv[1]
except IndexError:
    print "please give the name of the folder"
    exit()
    


if os.path.isfile('fin.traj'):
    calc = Vasp(restart=True)
    p= calc.get_atoms()
    p.set_initial_magnetic_moments(p.get_magnetic_moments())
    write('fin.traj',p)
    os.system('vfin.pl '+str(tar))

    os.system('cp init.traj fin.traj ' + str(tar))
    os.system('cp  ' + str(tar) +'/fe.dat  .')
    os.system('rm init.traj')
else:
    os.system('vfin.pl '+str(tar))
    os.system('cp init.traj ' + str(tar))
    ptmp=read(str(tar)+'/CONTCAR')
    pini=read(str(tar)+'/init.traj')
    mag=pini.get_initial_magnetic_moments()
    ptmp.set_initial_magnetic_moments(mag)
    write('init.traj', ptmp)

os.system('mv err* out* '+ str(tar))

