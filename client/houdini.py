from root import get_root_dir
import subprocess

def make_buildroot(target=None):
	command = ['make']

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

def start_vm(kernel="/buildroot/output/images/bzImage", drive="/buildroot/output/images/rootfs.ext2"):
	command = ['./start-qemu.sh', get_root_dir(kernel), get_root_dir(drive)]

	directory = get_root_dir("/scripts/")

	# Prepare the gnome-terminal command
	terminal_command = ['gnome-terminal', '--', 'bash', '-c', f'cd {directory} && {" ".join(command)}; exec bash']

	# Run the command
	result = subprocess.run(terminal_command)