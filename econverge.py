#!/usr/bin/env python

import os
import sys
import subprocess as sp
import matplotlib.pyplot as plt
import numpy as np

logfile='log'
try :
    logfile=sys.argv[1]
except IndexError:
    print "path of QE log file is not specified, use log under current directory "

keywd=' estimated scf accuracy '
ry2ev=13.605698066
sp.call("grep -B 2 \""+keywd+"\" " +logfile+"  > tmp",shell=True)
#print output
nitrs=int(sp.check_output("grep scf tmp|wc -l", shell= True))
#print nitrs
eng=[]
acc=[]

for i in range(nitrs):
    #print i
    en=sp.check_output("sed -n "+str(4*i+1)+"p tmp|awk '{print $(NF-1)}'",shell=True)
    eng.append(float(en)*ry2ev)
    ac=sp.check_output("sed -n "+str(4*i+3)+"p tmp|awk '{print $(NF-1)}'",shell=True)
    acc.append(float(ac)*ry2ev)
    #print en,ac

acc.pop(0)
den=[]
for i in range(nitrs-1):
    den.append(abs(eng[i+1]-eng[i]))
    print den[i]
    
its=np.linspace(0,nitrs-2,nitrs-1)
#print its
#print len(its), len(den),len(acc)
plt.semilogy(its,den,'r-',label='Energy difference')
plt.semilogy(its,acc,'b--',label='estimated scf accuracy')
plt.legend()

plt.savefig('ecvg.png')

