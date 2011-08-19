#!/bin/bash

INDIR=${1?'input dir required'}
OUTDIR="${INDIR%/}_out"
if [ ! -d $OUTDIR ]; then
	echo "output directory ${OUTDIR}"
	mkdir $OUTDIR
fi

for f in $(find $INDIR |egrep \.jpg$)
do
	python face_detect.py $f
	if [ -e out.jpg ]; then
		mv out.jpg $OUTDIR/$(basename $f) 
	fi
done
