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
    print p.get_magnetic_moments()
    if hasattr(p, 'get_magnetic_moments'):
        mag= p.get_magnetic_moments()
        print mag
        p.set_initial_magnetic_moments(mag)

os.chdir(cwd)

write('vasp.traj',p)

