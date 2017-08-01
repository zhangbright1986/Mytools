#!/usr/bin/env python
from ase.calculators.vasp import Vasp
from ase.io import read,write

p=read('CONTCAR')
pmag=read('init.traj')
mag=pmag.get_initial_magnetic_moments()
p.set_initial_magnetic_moments(mag)
write('new.traj',p)
print mag
