import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL

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

# Create a Docker client
client = docker.from_env()

def parse_trick_and_run(config_data):
    results = {}
    container = None

    for step in config_data['steps']:
        if 'spawnContainer' in step:
            try:
                container = client.containers.run(
                    image=step['spawnContainer']['image'],
                    name=step['spawnContainer']['name'],
                    command=step['spawnContainer']['cmd'],
                    working_dir=step['spawnContainer']['working_dir'],
                    detach=True
                )

                results['status'] = 'success'
                results['name'] = step['spawnContainer']['name']
                # container.wait(timeout=5)  # Wait for the container to finish
                # container.remove()  # Remove the container
            except Exception as e:
                results['status'] = 'failure'
                results['error'] = str(e)
            # finally:
                # if container is not None:
                    # container.kill(signal=SIGKILL)
                    # container.remove(force=True) 
    return results
        # elif 'container' in step:
        #     container = step['container']
        #     container_name = container['name']
        #     container_script = container['script'][0]
        #     bash_command = container_script['command']
        #     bash_args = container_script['args']
        #     try:
        #         # Execute the command inside the container
        #         exec_command = f'{bash_command} {" ".join(bash_args)}'
        #         exec_response = client.containers.run(container_name, command=exec_command)
        #         print(exec_response.decode())
        #     except Exception as e:
        #         print(f"Error executing command in container {container_name}: {e}")