import subprocess
from set_buildroot_pkg import *
from style import colors
from root import get_root_dir
import os
import multiprocessing
from set_kernel_version import *
import importlib
import config

def make_buildroot(target=None):
	# set_buildroot_pkg()
	# set_kernel_ver()
	command = ['make', '-j', f'{multiprocessing.cpu_count()}']
	# command = ['make']

	if target:
		command.append(target)

	# Run the make command
	result = subprocess.Popen(command, cwd=get_root_dir("/buildroot"), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
    encoding='utf-8', errors='replace')

	while True:
		realtime_output = result.stdout.readline()

		if realtime_output == '' and result.poll() is not None:
		    break

		if realtime_output:
		    print(realtime_output.strip(), flush=True)

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

    gnome_cmd = ["gnome-terminal", "--", *qemu_cmd]

    process = subprocess.Popen(gnome_cmd, stderr=subprocess.PIPE)

    _, error_output = process.communicate()

    if process.returncode == 0:
        print("VM started successfully.")
    else:
        print("Failed to start VM. Error message:")
        print(error_output.decode('utf-8').strip())

    return process



#update runc, docker-cli, docker engine
def set_buildroot_pkg():
	set_runc_version()
	set_docker_cli_version()
	set_docker_engine_version()

def set_kernel_ver():
	set_br2_linux_kernel_custom_version_value()
	set_br2_package_host_linux_headers_custom()
	set_br2_toolchain_headers_at_least()

def help_():
	return 1

def exit_program():
	print(colors.BOLD + colors.GREEN + "\nExiting" + colors.RESET)
	exit(0)

def reload_config():
	importlib.reload(config)
	KERNEL_VERSION = config.KERNEL_VERSION

def get_response(path):
	requests.get(VM_URL + path)


def run_trick():
	return 0