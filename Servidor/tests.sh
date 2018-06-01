#!/bin/bash
echo "STARTING TESTS"
echo "-----------------------PERCENTAGES TEST-----------------------"
python3 Servidor/test_porcentajes.py
echo "-----------------------AGREED_EMOTION TEST-----------------------"
python3 Servidor/test_consensuada.py
echo "-----------------------MAIN_EMOTION TEST-----------------------"
python3 Servidor/test_mayoritaria.py
echo "-----------------------WORDS TEST-----------------------"
python3 Servidor/test_palabras.py
echo "-----------------------SENTENCES TEST-----------------------"
python3 Servidor/test_frase.py