#!/bin/bash

lista=`ls $1`

for arquivo in $lista; do
	linhas=`cat $1$arquivo| sed 's/\ /_/g'`
	for j in $linhas; do
		#para comparacao
		#echo $j|sed 's/_/\ /g'
		echo $j|sed 's/^1_/0_/g'|sed 's/^2_/1_/g'|sed 's/^4_/2_/g'|sed 's/_/\ /g' >> $2$arquivo
	done;
done;
