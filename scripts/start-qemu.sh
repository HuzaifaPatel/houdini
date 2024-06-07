qemu-system-x86_64 \
	-enable-kvm \
	-m 8000 \
	-kernel $1 \
	-drive file=$2,if=virtio,format=raw \
	-append "rootwait root=/dev/vda console=tty1 console=ttyS0" \
	-serial mon:stdio \
	-net nic,model=virtio \
	-net user,hostfwd=tcp::5000-:5000 \
	-nographic