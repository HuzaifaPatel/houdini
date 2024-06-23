import subprocess
from buildroot_package_manager import *
from style import Style
from path_manager import get_absolute_path
import os
import multiprocessing
from kernel_configurator import *
import importlib
from config import PORT

class BuildrootManager:
	def __init__(self):
		self.cpu_count = multiprocessing.cpu_count()

	def make_buildroot(self, target=None):
		self.set_buildroot_pkg()
		self.set_kernel_ver()
		self.make_olddefconfig()

		command = ['make', '-j', f'{self.cpu_count}']

		if target:
			command.append(target)

		# Run the make command
		result = subprocess.Popen(command, cwd=BUILDROOT_PATH, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
	    encoding='utf-8', errors='replace')

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

	def start_vm(self, kernel=get_absolute_path("/buildroot/output/images/bzImage"), drive=get_absolute_path("/buildroot/output/images/rootfs.ext2")):
	    qemu_cmd = [
	        "qemu-system-x86_64",
	        "-enable-kvm",
	        "-m", "5000",
	        "-kernel", kernel,
	        "-drive", f"file={drive},if=virtio,format=raw",
	        "-append", "rootwait root=/dev/vda console=tty1 console=ttyS0 quiet loglevel=3",
	        "-serial", "mon:stdio",
	        "-net", "nic,model=virtio",
	        "-net", "user,hostfwd=tcp::{}-:{}".format(PORT, PORT),
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

	def set_buildroot_pkg(self):
		if os.path.exists(BUILDROOT_OUTPUT_BUILD):
			BuildrootPackageManager.set_runc_version()
			BuildrootPackageManager.set_docker_cli_version()
			BuildrootPackageManager.set_docker_engine_version()

	def set_kernel_ver(self):
		KernelConfigurator.set_br2_linux_kernel_custom_version_value() # this is good
		KernelConfigurator.set_br2_package_host_linux_headers_custom()
		KernelConfigurator.set_br2_toolchain_headers_at_least()