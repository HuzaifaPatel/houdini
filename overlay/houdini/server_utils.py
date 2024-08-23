import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL
import subprocess
container = None
# Create a Docker API client
client = docker.APIClient(base_url='unix://var/run/docker.sock')

def is_service_running(service_name):
    result = subprocess.run(['pgrep', '-f', service_name], check=True, stdout=subprocess.PIPE)

    if not result.returncode:
        return True
    return False


def get_version():
    version_info = {}
    for key, value in versions.items():
        result = subprocess.run(value, check=True, stdout=subprocess.PIPE)
        version_info[key] = result.stdout.decode('utf-8').strip()
    
    return version_info

def run_command_in_container(container, cmd):
    """Run a command in the specified container and return the output."""
    # Create an exec instance
    client = docker.from_env()

    exec_id = client.api.exec_create(
        container.id,
        cmd,
        stdout=True,
        stderr=True
    )
    
    # Start the exec instance
    output = client.api.exec_start(exec_id, detach=False, tty=False)
    print(output.decode('utf-8'))

def run_command_in_host(cmd_on_host):
    # Run the ifconfig command
    try:
        result = subprocess.run(cmd_on_host, capture_output=True, text=True, check=True)
        print("HOST")
        # Print the output of the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Print any errors that occur
        print(f'Error occurred: {e}')

def parse_trick_and_run(trick_data, PRIV_MODE):
    # Create a Docker client
    client = docker.from_env()
    client.images.pull('ubuntu')
    results = {}
    container_name = trick_data.get('name')
    docker_args = trick_data.get('docker_args', {})
    cmd_on_host = trick_data['command_on_host']['command']
    cmd_in_container = trick_data['command_in_container']['command']
     
    # Check if the container with the given name already exists.
    # if it exists, send SIGKILL to it first.
    try:
        existing_container = client.containers.get(container_name)
        print(f"Container {container_name} already exists. Removing it.")
        if existing_container.status == 'running':
            existing_container.kill(signal=SIGKILL)
        existing_container.remove(force=True)
    except docker.errors.NotFound:
        print(f"No existing container named {container_name} found. Proceeding to create a new one.")

    try:
        global container
        run_command_in_host(cmd_on_host)
        container = client.containers.run(**docker_args)
        run_command_in_container(container, cmd_in_container)

        results['status'] = 'success'
        results['output'] = 'ok'
    except Exception as e:
        print(f"Failed to run container {container_name}: {e}")
        results['name'] = container_name
        results['status'] = 'failure'

    return results
