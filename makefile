CC=gcc
LDFLAGS=-lvirt
GUESTFS =-lguestfs

houdini: main.o client.o client.h vm.o vm.h install_libvirt_dev install_libguestfs_dev
	gcc -o houdini main.c client.c client.h vm.c vm.h ${LDFLAGS} ${GUESTFS}

install_libvirt_dev:
	dpkg -s libvirt-dev >/dev/null 2>&1 || sudo apt-get -y install libvirt-dev

install_libguestfs_dev:
	dpkg -s libguestfs-tools >/dev/null 2>&1 || sudo apt-get -y install libguestfs-tools
# also add sudo apt-get install libguestfs-dev
# sudo apt-get install libnbd-dev

clean:
	@if [ -f houdini ]; then rm houdini; fi
	@if [ -f main.o ]; then rm main.o; fi
	@if [ -f client.o ]; then rm client.o; fi
	@if [ -f lol.qcow2 ]; then rm lol.qcow2; fi
