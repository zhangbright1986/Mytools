#!/usr/bin/env python
from ase import Atoms, Atom
from ase.calculators.vasp import Vasp
from ase.io import read,write

            
p=read('init.traj')
calc = Vasp(prec='normal',
            encut=400.0,
            xc='PBE',
            lreal='Auto',
            kpts=[3,3,1],
            nsw = 200,
            ibrion = 2,
            amix_mag = 0.800000,
            bmix = 0.000100,
            bmix_mag= 0.000100,
            amix = 0.20000,
            sigma = 0.050000,
            ediff = 1.00e-05,
            ediffg = -2.00e-02,
            algo ='fast',
            ismear = 0,
            nelm = 250,
            ncore = 16,
            lasph= True,
            ldautype = 2,
            lmaxmix = 4,
            lorbit = 11,
            ldauprint = 2,
            ldau_luj={'Fe':{'L':2,  'U':5.0, 'J':1.0},
                      'Co':{'L':2, 'U':4.0, 'J':1.0},
                      'Au':{'L':-1, 'U':0.0, 'J':0.0},
                      'O':{'L':-1, 'U':0.0, 'J':0.0}
                      },
            lvtot = False,
            lwave = False,
            lcharg = False,
)
calc.calculation_required = lambda x, y: True
p.set_calculator(calc)
pe=p.get_potential_energy()

mag=p.get_magnetic_moments()
p.set_initial_magnetic_moments(mag)

write('fin.traj',p)

print "Energy = "+str(pe)

