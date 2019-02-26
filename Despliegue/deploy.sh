#!/bin/bash

mkdir -p ./mkosi.extra/Servidor
mount -o bind,ro ../Servidor ./mkosi.extra/Servidor
mkosi -f
umount mkosi.extra/Servidor
