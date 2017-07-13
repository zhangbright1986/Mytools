#!/usr/bin/env python
from ase.io import read, write
from ase.utils.geometry import sort
from ase.data import chemical_symbols
import sys
import argparse

# filein='POSCAR'
# fileout='POSCAR.new'
parser = argparse.ArgumentParser()
parser.add_argument("filein", nargs="?", help='reading file', default='POSCAR')
parser.add_argument("fileout", nargs="?", help='output file', default='POSCAR.new')
parser.add_argument("-s", "--seq", nargs='+', help="elements order", default=None)
args = parser.parse_args()
print args.filein, args.fileout, args.seq

print "Read structure from " + args.filein
if args.seq:
    print "Sorting strcuture in the order of " + str(args.seq)
else:
    print "Sorting strucutre in order of chemical symbols"
print "Write sorted strcuture to " + args.fileout

p = read(args.filein)
pcopy = p.copy()
pcopy = sort(pcopy)
plist = pcopy.get_chemical_symbols()
# print plist
plist = list(set(plist))

if args.seq:
    potdict = {}
    val = 1

    rlist = list(set(args.seq))
    if plist not in rlist:
        print "Warning: Sorting list doesn't include all elements in input file"

    for si in args.seq:
        if si in chemical_symbols:
            # print si, val
            potdict.update({si: val})
            val += 1
        else:
            print si + " is not a chemical symbol and will be skipped"

    # print potdict
    for pi in p:
        for key in potdict:
            if pi.symbol == key:
                pi.tag = potdict[key]

    p = sort(p, tags=p.get_tags())
else:
    p = sort(p)

write(args.fileout, p)
