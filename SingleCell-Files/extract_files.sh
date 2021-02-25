#!/bin/bash

cd HCA_matrices

for i in *
do
	if [ -d "$i" ]; then
		cd $i
		rm *.csv.zip
		unzip *
		rm *.mtx.zip
		mv */* .
		rm -rf *.mtx
		gzip -dk cells.tsv.gz
		n=$(sed -n $'1s/\t/\\\n/gp' cells.tsv | grep -nx 'project.provenance.document_id' | cut -d: -f1)
		id=$(head -n 2 cells.tsv | tail -n 1 | cut -f$n -d$'\t')
		rm cells.tsv
		cd ..
		mv $i $id
	fi
done
