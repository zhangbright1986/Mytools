#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filein", nargs="?", help='readin POTCAR', default='POTCAR')
args = parser.parse_args()
filein = args.filein

rin = open(filein, 'r')

elmlist = []
titlist = []
potline = ""
for line in rin:
    potline += line
    buf = line.split()
    if "TITEL" in buf:
        elm = buf[3]
        tit = buf[2:]
        elmlist.append(elm)
        titlist.append(tit)
    if 'End' in buf and 'Dataset' in buf:
        fileout = "POTCAR." + elm
        f = open(fileout, 'w')
        f.write(potline)
        f.close()
        potline = ""

rin.close()

print "POTCAR has been decomposed to:"
for ti in range(len(titlist)):
    print "POTCAR." + elmlist[ti] + ': ' + ' '.join(titlist[ti])
