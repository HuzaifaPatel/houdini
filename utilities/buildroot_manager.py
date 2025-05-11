import subprocess
from buildroot_package_manager import *
from style import Style
from path_manager import *
import os
import multiprocessing
import importlib
from houdini_config import PORT, VM_RAM, CPU_CORES, KERNEL_VERSION
import shutil
import time

class BuildrootManager:
	def __init__(self):
		self.cpu_count = multiprocessing.cpu_count() - 1

	def make(self, command, target=None):
		if target:
			command.append(target)
		result = subprocess.Popen(command, cwd=BUILDROOT_PATH, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, encoding='utf-8', errors='replace')

		while True:
			realtime_output = result.stdout.readline()

			if realtime_output == '' and result.poll() is not None:
			    break

			if realtime_output:
			    print(realtime_output.strip(), flush=True)

		# Output the results
		if result.returncode == 0:
			Style.print_color("\nMake succeeded\n", 'green')
		else:
			Style.print_color("\nMake failed\nError:\n", "red")
			print(result.stderr)

	# this updates overlay with the docker version of the user's choice
	def run_get_docker(self):
	    # Run the shell script first
	    result = subprocess.run(['bash', 'get_docker.sh'], cwd=SCRIPTS)

	    if result.returncode != 0:
	        print("get_docker.sh failed!")
	        return
	    else:
	    	print("Moved Docker files to overlay")


	def make_filesystem(self):
		self.run_get_docker()
		command = ['make', f'O={FILESYSTEM_PATH}', '-j', f'{self.cpu_count}']
		# self.set_buildroot_pkg()
		# shutil.copy(BUILDROOT_CONFIG_FILE, FILESYSTEM_PATH)
		self.make_olddefconfig()
		self.make(command, 'rootfs-ext2')

	def make_olddefconfig(self):
		command = ['make', 'olddefconfig', '-j', f'{self.cpu_count}']

		# Run the make command
		result = subprocess.run(command, cwd=BUILDROOT_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

		# Output the results
		if result.returncode == 0:
			Style.print_color("Make olddefconfig command succeeded", 'green')
		else:
			Style.print_color("Make olddefconfig command failed", 'red')
			Style.print_color("Error:", 'red')
			print(result.stderr)

	def start_vm(self, kernel=get_absolute_path(f"/kernels/{KERNEL_VERSION}/arch/x86/boot/bzImage"), drive=get_absolute_path("/buildroot/output/images/rootfs.ext2")):
	    qemu_cmd = [
	        "qemu-system-x86_64",
	        "-smp", str(CPU_CORES),
	        "-m", str(VM_RAM),
	        "-kernel", kernel,
	        "-drive", f"file={drive},if=virtio,format=raw",
	        "-append", "apparmor=1 security=apparmor rootwait root=/dev/vda console=tty1 console=ttyS0 loglevel=0 cgroup_enable=cpuset cgroup_enable=memory",
	        "-serial", "mon:stdio",
	        "-net", "nic,model=virtio",
	        "-net", f"user,hostfwd=tcp::{PORT}-:{PORT}",
	        "-nographic",
	        "-virtfs", "local,path=/home/huzi/Desktop,mount_tag=hostshare,security_model=mapped-file,id=hostshare"
	    ]

	    terminal_cmd = [
	        "gnome-terminal", "--tab", "--",
	        *qemu_cmd
	    ]

	    subprocess.Popen(terminal_cmd)


	def set_kernel_ver(self):
		KernelConfigurator.set_br2_linux_kernel_custom_version_value() # this is good
		KernelConfigurator.set_br2_package_host_linux_headers_custom()
		KernelConfigurator.set_br2_toolchain_headers_at_least()