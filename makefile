CC=gcc
LDFLAGS=-lvirt
GUESTFS =-lguestfs

houdini: install_libelf-dev install_lib_ssl install_libvirt_dev install_libguestfs_dev install_guest_fs install_libnbd_dev main.o client.o client.h vm.o vm.h
	gcc -o houdini main.c client.c client.h vm.c vm.h ${LDFLAGS} ${GUESTFS}

install_libvirt_dev:
	sudo apt-get install -y libvirt-dev

install_libguestfs_dev:
	sudo apt-get install -y libguestfs-tools

install_guest_fs:
	sudo apt-get install -y libguestfs-dev

install_libnbd_dev:
	sudo apt-get install -y libnbd-dev

install_lib_ssl:
	sudo apt-get install -y libssl-dev

install_libelf-dev:
	sudo apt-get install -y libelf-dev

install_qemu:
	sudo apt-get install -y qemu

install_qemu:
	sudo apt-get install -y qemu-kvm

clean:
	@if [ -f houdini ]; then rm houdini; fi
	@if [ -f main.o ]; then rm main.o; fi
	@if [ -f client.o ]; then rm client.o; fi
	@if [ -f lol.qcow2 ]; then rm lol.qcow2; fi
