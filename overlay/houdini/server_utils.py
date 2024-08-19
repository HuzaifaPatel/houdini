import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL
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


def parse_trick_and_run(trick_data, PRIV_MODE):
    # Create a Docker client
    client = docker.from_env()
    client.images.pull('ubuntu')
    results = {}
    container_name = trick_data.get('name')
    docker_args = trick_data.get('docker_args', {})
    cmd_to_execute = trick_data['command_to_execute']['command']
     
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
    
        # if PRIV_MODE:
            # container_kwargs['privileged'] = True

        # if APPARMOR:
            # container_kwargs['security_opt'].append('apparmor=docker-default')

        container = client.containers.run(**docker_args)

        # Create and run an exec instance to list files in the root directory
        exec_id = client.api.exec_create(
            container.id,
            cmd=cmd_to_execute,
            stdout=True,
            stderr=True
        )
        output = client.api.exec_start(exec_id['Id'], detach=False).decode('utf-8')
        print(output)
        results['status'] = 'success'
        results['output'] = output
    except Exception as e:
        print(f"Failed to run container {container_name}: {e}")
        results['name'] = container_name
        results['status'] = 'failure'

    return results
