#!/bin/bash
cd Servidor
source entorno/bin/activate
echo "STARTING TESTS"
echo "-----------------------PERCENTAGES TEST-----------------------"
python test_porcentajes.py
echo "-----------------------AGREED_EMOTION TEST-----------------------"
python test_consensuada.py
echo "-----------------------MAIN_EMOTION TEST-----------------------"
python test_mayoritaria.py
echo "-----------------------WORDS TEST-----------------------"
python3 test_palabras.py
echo "-----------------------SENTENCES TEST-----------------------"
python3 test_frase.py