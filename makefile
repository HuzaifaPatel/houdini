CC=gcc
LDFLAGS=-lvirt
GUESTFS =-lguestfs

houdini: install_libelf-dev install_lib_ssl install_libvirt_dev install_libguestfs_dev install_guest_fs install_libnbd_dev install_qemu install_qemu_kvm install_pip_three install_beautifulsoup_four main.o client.o client.h vm.o vm.h view.c view.h
	gcc -o houdini main.c client.c vm.c view.c ${LDFLAGS} ${GUESTFS} 
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

install_qemu_kvm:
	sudo apt-get install -y qemu-kvm

install_jq:
	sudo apt-get install -y jq

install debootstrap:
	sudo apt-get install -y debootstrap

install_pip_three:
	sudo apt-get install -y python3-pip

install_apt_checker:
	sudo apt-get install -y apt-cacher-ng
	sudo systemctl start apt-cacher-ng

install_beautifulsoup_four:
	pip3 install beautifulsoup4

install debmirror:
	sudo apt-get install -y debmirror
	
clean:
	@if [ -f houdini ]; then rm houdini; fi
	@if [ -f main.o ]; then rm main.o; fi
	@if [ -f client.o ]; then rm client.o; fi
