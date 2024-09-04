import socket
import os
import docker
check_mark = '\u2713'
x_button = "\u2717"

def check_server(host='localhost', port=8000):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.settimeout(5)  # Set a timeout for the connection attempt
		try:
			s.connect((host, port))
			return True
		except (socket.timeout, ConnectionRefusedError):
			return False

def find_file(filename):
	for root, dirs, files in os.walk('/'):  # Start searching from the root directory
		if filename in files:
			print(f"{filename} exists on Host {check_mark}")
			return True
	print("File Does not Exist")
	return False

def check_python3_in_container(container_name):
	client = docker.from_env()  # Connect to Docker
	try:
		container = client.containers.get(container_name)  # Get the container by ID
        # Run a command in the container to check if python3 exists
		exit_code, output = container.exec_run('which python3')
		if exit_code == 0:
			print(f"Python 3 is installed in the container. {check_mark}")
			return True  # Python 3 exists
		else:
			print("Python 3 is not installed in the container.")
			return False  # Python 3 does not exist
	except docker.errors.NotFound:
		print(f"Container with ID '{container_name}' not found.")
		return False
	except Exception as e:
		print(f"An error occurred: {e}")
		return False