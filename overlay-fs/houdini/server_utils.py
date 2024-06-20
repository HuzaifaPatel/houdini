import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL
container = None
# Create a Docker API client
client = docker.APIClient(base_url='unix://var/run/docker.sock')

def is_service_running(service_name):
    try:
        subprocess.run(['systemctl', 'is-active', service_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def get_version():
    version_info = {}
    for key, value in versions.items():
        result = subprocess.run(value, check=True, stdout=subprocess.PIPE)
        version_info[key] = result.stdout.decode('utf-8').strip()
    
    return version_info


def parse_trick_and_run(config_data):
    # Create a Docker client
    client = docker.from_env()
    # Pull the 'ubuntu' image
    client.images.pull('ubuntu')
    results = {}

    for step in config_data['steps']:
        if 'spawnContainer' in step:

            container_name = step['spawnContainer']['name']

            # Check if the container with the given name already exists
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
                container = client.containers.run(
                    image=step['spawnContainer']['image'],
                    name=step['spawnContainer']['name'],
                    command=step['spawnContainer']['cmd'],
                    working_dir=step['spawnContainer']['working_dir'],
                    detach=True,
                    tty=True
                )
                print("CONTAINER STARTED")
                results['status'] = 'success'
                results['name'] = step['spawnContainer']['name']
            except Exception as e:
                results['name'] = step['spawnContainer']['name']
                results['status'] = 'failure'
            finally:
                if container is not None:
                    container.kill(signal=SIGKILL)
                    container.remove(force=True) 

    return results