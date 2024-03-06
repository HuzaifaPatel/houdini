CC=gcc
LDFLAGS=-lvirt

houdini: main.o client.o client.h vm.c vm.h install_libvirt_dev 
	gcc -o houdini main.c client.c client.h vm.c vm.h ${LDFLAGS}

install_libvirt_dev:
	dpkg -s libvirt-dev >/dev/null 2>&1 || sudo apt-get -y install libvirt-dev

clean:
	@if [ -f houdini ]; then rm houdini; fi
	@if [ -f main.o ]; then rm main.o; fi
	@if [ -f client.o ]; then rm client.o; fi
