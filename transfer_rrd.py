#!/usr/bin/python

import os, sys

srcdir = sys.argv[1]
tgthost = sys.argv[2]
tgtdir = sys.argv[3]

print "Copy from", srcdir, " to %s:%s" % (tgthost,tgtdir)

def cmd(c):
    print "Execute:", c
    os.system(c)

for root, dirs, files in os.walk(srcdir):
    rr = os.path.relpath(root, srcdir)
    print rr, root, srcdir
    for di in dirs:
        d = os.path.join(tgtdir, rr, di)
        print "Creating dir:", d
        cmd( "ssh " + tgthost + " mkdir -p " + d )
    print

    for fi in files:
        ftgt = os.path.join(tgtdir, rr, fi)
        fsrc = os.path.join(root, fi)
        if os.path.splitext(fi)[1] == ".rrd":
            print fsrc, "-->", ftgt
            cmd( "rrdtool dump '" + fsrc + "' | ssh " + tgthost + " rrdtool restore - '" + ftgt + "'" )
