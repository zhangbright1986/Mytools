#!/usr/bin/env python
import os
from ase.io import read, write
from ase.calculators.vasp import Vasp
import sys


calc=Vasp(restart=True)
cwd=os.getcwd()

tar=cwd
try:
    tar=sys.argv[1]
except IndexError:
    print "Currnet directory will be used to extract VASP calculation"

if os.path.isfile(tar+'/OUTCAR'):
    os.chdir(tar)
    calc = Vasp(restart=True)
    p=calc.get_atoms()
    if hasattr(p, 'get_magnetic_moments'):
        p.set_initial_magnetic_moments = p.get_magnetic_moments()

os.chdir(cwd)

write('vasp.traj',p)

    

#p=calc.get_atoms()
'''
isf os.path.isfile('fin.traj'):
    calc = Vasp(restart=True)
    p= calc.get_atoms()
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
'''
