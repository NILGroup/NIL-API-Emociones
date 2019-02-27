#!/bin/bash

rm -rf ./mkosi.extra/Servidor
mkdir -p ./mkosi.extra/Servidor
git --work-tree=./mkosi.extra/ checkout HEAD -- Servidor
mkosi -f
