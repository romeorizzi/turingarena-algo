#!/bin/bash

NUM="$1"
shift

if [ "z$NUM" == "z0" ] ; then
	cat << EOF
4 3
1 2
2 1 2
1 2
2 1 3
EOF
	exit 0
fi

if [ "z$NUM" == "z1" ] ; then
	cat << EOF
4 3
1 2
2 1 3
0
1 1
EOF
	exit 0
fi

if [ "z$NUM" == "z2" ] ; then
	./gen/generatore1 "$@"
	exit 0
fi

if [ "z$NUM" == "z3" ] ; then
	./gen/generatore2 "$@"
	exit 0
fi

