#!/usr/bin/python
import os, sys

if len(sys.argv) != 3:
	print "Usage: file-sort-and-remove-duplicate-lines.py inputfile outputfile"
	sys.exit()
if not os.access(sys.argv[1], os.F_OK):
	print "Error: input file '%s' does not exist"% sys.argv[1]
	sys.exit()
if not os.access(sys.argv[1], os.R_OK):
	print "Error: input file '%s' is not readable"% sys.argv[1]
	sys.exit()
if os.access(sys.argv[2], os.F_OK) and not os.access(sys.argv[2], os.W_OK):
	print "Error: output file '%s' is not writable"% sys.argv[2]
	sys.exit()

contents = {}
with open(sys.argv[1]) as f:
	for line in f:
		contents[line] = 1
	sorted_contents = sorted(contents.keys())
with open(sys.argv[2], 'w') as f:
	for line in sorted_contents:
		f.write(line)
