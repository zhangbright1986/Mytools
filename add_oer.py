#!/usr/bin/env python

from ase.io import read,write
from ase import Atoms
import sys
import os
from shutil import copyfile

cwd=os.getcwd()
basefile='init.traj'
submit=False

try:
    p0=read(basefile)
except IOError:
    print "check existence of init.traj"
    exit()

tar=81
try:
    tar=int(sys.argv[1])
except IndexError:
    print "default index: 81"

tarpos=p0[tar].position

ado=Atoms('O', positions=[tarpos+[ 0.01008241,  0.01003518,  1.62578429]])

adoh=Atoms('OH', positions=[tarpos+[ 0.10168336,  0.12323385,  1.81387145],\
        tarpos+[ 0.90622851, -0.05146373,  2.32943537]])

adooh=Atoms('OOH', positions=[tarpos+[ 0.27268263,  0.4223962 ,  1.96974462],\
        tarpos+[0.02300319, -0.63465221,  2.85712563],\
        tarpos+[ 0.239776  , -0.20784769,  3.71486634]])

pado=p0+ado
padoh=p0+adoh
padooh=p0+adooh

ads_dict={'o':pado,
        'oh':padoh,
        'ooh':padooh}
for key in ads_dict.keys():
    if not os.path.isdir(cwd+'/'+key):
        os.mkdir(cwd+'/'+key)
    write(cwd+'/'+key+'/init.traj', ads_dict[key])
    copyfile('/home/liangzha/STR/Ru-STO-alloy/.script/esp.sub', cwd+'/'+key+'/esp.sub')
    if submit:
        os.chdir(cwd+'/'+key)
        os.system('sbatch esp.sub')


os.chdir(cwd)

    
#adoh=

#adooh=

