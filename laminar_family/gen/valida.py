#!/usr/bin/env python2

from limiti import *

from sys import argv, exit, stderr
import os

def usage():
    print >> stderr, "Usage: %s file_input.txt" % \
        os.path.basename(argv[0])
    exit(1)

def run(f):
    prima  =[int(x) for x in f[0].split()]    
    assert(len(prima) == 2)
    N,M = prima
    assert(1 <= N <= MAXN)
    assert(1 <= M <= MAXM)
    assert(len(f)==1+N)
    for i in xrange(N):
        riga=[int(x) for x in f[i+1].split()]
        num=riga[0]
        assert(len(riga)==1+num)
        assert(0<=num<=M)
        for j in xrange(num):
            assert(1<=riga[1+j]<=M)

    return 0 # Input corretto

if __name__ == "__main__":
    if len(argv) < 2:
        usage()

    try:
        import psyco
        psyco.full()
    except ImportError:
        stderr.write("Installa psyco per un po' di velocita` in piu`.\n")

    f = open(argv[1]).readlines()
    exit(run(f))


