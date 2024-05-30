from root import get_root_dir
from update_buildroot_packages import update_runc_version, update_docker_cli_version, update_docker_engine_version
import subprocess

def make_buildroot(target=None):
	command = ['make', '-j', '10']

	if target:
		command.append(target)

	# Run the make command
	result = subprocess.run(command, cwd=get_root_dir("/buildroot"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

	# Output the results
	if result.returncode == 0:
		print("Make command succeeded")
	else:
		print("Make command failed")
		print("Error:")
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

def start_vm(kernel="/buildroot/output/images/bzImage", drive="/buildroot/output/images/rootfs.ext2"):
	command = ['./start-qemu.sh', get_root_dir(kernel), get_root_dir(drive)]

	directory = get_root_dir("/scripts/")

	# Prepare the gnome-terminal command
	terminal_command = ['gnome-terminal', '--', 'bash', '-c', f'cd {directory} && {" ".join(command)}; exec bash']

	# Run the command
	result = subprocess.run(terminal_command)


#update docker-cli, docker engine, runc
def update_packages():
	update_runc_version()
	update_docker_cli_version()
	update_docker_engine_version()
