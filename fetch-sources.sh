#!/bin/sh

wget https://buildroot.org/downloads/buildroot-2023.02.9.tar.xz && \
    tar xvf buildroot-2023.02.9.tar.xz && \
    mv buildroot-2023.02.9 buildroot

cp .config buildroot/

wget https://download.qemu.org/qemu-8.2.0.tar.xz && \
    tar xvf qemu-8.2.0.tar.xz && \
    mv qemu-8.2.0 qemu

patch -p1 -d qemu < qemu-usb-flagbrah.patch
