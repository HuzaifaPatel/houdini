import subprocess
from update_buildroot_packages import *
from style import colors
from root import get_root_dir
import os
import multiprocessing

def make_buildroot(target=None):
	command = ['make', '-j', f'{multiprocessing.cpu_count()}']

	if target:
		command.append(target)

	# Run the make command
	result = subprocess.run(command, cwd=get_root_dir("/buildroot"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

	# Output the results
	if result.returncode == 0:
		print(colors.BOLD + colors.GREEN  + "\nMake succeeded" + colors.RESET + "\n")
	else:
		print(colors.BOLD + colors.RED + "\nMake failed" + colors.RESET)
		print(colors.BOLD + colors.RED + "\nError:" + colors.RESET + "\n")
		print(result.stderr)


def make_olddefconfig():
	command = ['make', 'olddefconfig', '-j', '20']

	# Run the make command
	result = subprocess.run(command, cwd=get_root_dir("/buildroot"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

	# Output the results
	if result.returncode == 0:
		print("Make olddefconfig command succeeded")
	else:
		print("Make olddefconfig command failed")
		print("Error:")
		print(result.stderr)


def start_vm(kernel=get_root_dir("/buildroot/output/images/bzImage"), drive=get_root_dir("/buildroot/output/images/rootfs.ext2")):
    qemu_cmd = [
        "qemu-system-x86_64",
        "-enable-kvm",
        "-m", "10000",
        "-kernel", kernel,
        "-drive", f"file={drive},if=virtio,format=raw",
        "-append", "rootwait root=/dev/vda console=tty1 console=ttyS0 quiet loglevel=3",
        "-serial", "mon:stdio",
        "-net", "nic,model=virtio",
        "-net", "user,hostfwd=tcp::5000-:5000",
        "-cpu", "host",
        "-nographic"
    ]
    subprocess.run(qemu_cmd)


#update runc, docker-cli, docker engine
def update_packages():
	update_runc_version()
	update_docker_cli_version()
	update_docker_engine_version()


def exit_program():
	print(colors.BOLD + colors.GREEN + "\nExiting" + colors.RESET)
	exit(0)