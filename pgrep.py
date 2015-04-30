#!/usr/bin/python

import os.path
import sys

filename=""
pattern=""
filename=sys.argv[2]
pattern=sys.argv[1]

if  not os.path.isfile(filename):
    print "file doesn\'t exist"
    sys.exit(2)
output = open(filename)
mystr=pattern
for line in output:
    if mystr in line: print line

print "bye"
#print 'Argument List:', sys.argv[1]
output.close()
