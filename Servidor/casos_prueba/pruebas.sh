#!/bin/bash

rm -r resultados
mkdir resultados
for i in *;
do
	if [ $i != 'pruebas.sh' ] && [ $i != 'resultados' ]; then
		echo $i
		python3 ../traductor.py $i > resultados/$i
	fi;
done