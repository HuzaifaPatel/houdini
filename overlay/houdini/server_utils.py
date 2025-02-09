import subprocess
import yaml
from config import *
import docker
from signal import SIGKILL
import subprocess
import io
import tarfile
import os
import codecs
import sys
import threading
from docker.types import Ulimit
check_mark = '\u2713'
x_button = "\u2717"
client = docker.from_env()

def is_service_running(service_name):
    result = subprocess.run(['pgrep', '-f', service_name], check=True, stdout=subprocess.PIPE)

    if not result.returncode:
        return True
    return False


def build_docker_image(dockerfile_path, image_name):
    try:
        # Build the Docker image
        print("Creating Docker Image")
        client.images.build(path=".", tag=image_name, rm=True)
        print(f"Image '{image_name}' built successfully. {check_mark}")
    except docker.errors.BuildError as e:
        print(f"Error building Docker image: {e}")



def run_docker_container(image_name, container_name, network_mode, read_only, security_opt, pid_mode, cpu_shares, volumes, mem_limit, cpuset_cpus, cpu_quota, cpu_period, cap_add, cap_drop, privileged, user, pids_limit, ipc_mode, path):
    try:

        container = client.containers.run(
            image_name,
            name=container_name,
            detach=True, 
            network_mode=network_mode, 
            read_only=read_only, 
            security_opt=security_opt,
            pid_mode=pid_mode, 
            cpu_shares=cpu_shares,
            volumes=volumes,
            mem_limit=mem_limit,
            cpuset_cpus=cpuset_cpus,
            cpu_quota=cpu_quota,
            cpu_period=cpu_period,
            cap_add=cap_add,
            cap_drop=cap_drop,
            privileged=privileged,
            user=user,
            pids_limit=pids_limit,
            ipc_mode=ipc_mode
        )


        print(f"Container '{container_name}' started successfully. {check_mark}")

        if image_name == "cpu_shares":
            run_program_on_vm(path)

        # Attach to the container's stdout
        for chunk in codecs.iterdecode(container.attach(stdout=True, stderr=False, stream=True, logs=False), "utf-8"):
            sys.stdout.write(chunk)

        # Wait for the container to finish
        exit_status = container.wait()
        
        # Get the exit code
        exit_code = exit_status['StatusCode']
        print(f"Container exited with code: {exit_code}")
        

        # Check if the container exited properly
        if exit_code == 0:
            print("Container exited successfully.")
        else:
            print("Container exited with errors.")

        return container
    except docker.errors.APIError as e:
        print(f"Error running Docker container: {e}")


def send_file_to_container(container_name, file_path, target_file_name, target_directory='/'):
    client = docker.from_env()
    container = client.containers.get(container_name)

    # Open the file to send
    with open(file_path, 'rb') as file_data:
        # Create a tar archive of the file
        tar_data = io.BytesIO()
        with tarfile.open(fileobj=tar_data, mode='w') as tar:
            # Use target_file_name for the file inside the container
            tar.add(file_path, arcname=target_file_name)
        
        tar_data.seek(0)
        
        # Upload the file to the container
        try:
            container.put_archive(target_directory, tar_data)
            print(f"File {file_path} successfully uploaded to {target_directory}/{target_file_name} in container {container_name} {check_mark}")
        except docker.errors.APIError as e:
            print(f"Error uploading file: {e}")


def run_command_in_container(container, command):
    exec_command = f"bash -c '{command}'"

    try:
        # Execute the command inside the container
        result = container.exec_run(exec_command, stdout=True)
        print(result.output.decode())
    except docker.errors.APIError as e:
        print(f"Error executing command in container: {e}")


def check_if_container_is_running(container_name):
    # Check if the container with the given name already exists. If it exists, send SIGKILL to it first.
    try:
        existing_container = client.containers.get(container_name)
        print(f"Container {container_name} already exists. Removing it.")
        if existing_container.status == 'running':
            existing_container.kill(signal=SIGKILL)
        existing_container.remove(force=True)
    except docker.errors.NotFound:
        print(f"No existing container named {container_name} found. Proceeding to create a new one.")

def delete_docker_image(image_identifier):
    try:
        # Get the image
        image = client.images.get(image_identifier)
        
        # Remove the image
        client.images.remove(image.id)
        print(f"Successfully removed image: {image.id}")
    except docker.errors.ImageNotFound:
        print(f"Image '{image_identifier}' not found.")
    except docker.errors.APIError as e:
        print(f"Error occurred: {e}")

def parse_trick_and_run(trick_data, args):
    container_name = args.get('container_name')

    # next three function calls are generic. They will never be different
    check_if_container_is_running(container_name)

    original_directory = os.getcwd()
    os.chdir(trick_data['trick'][0]['path'])
    build_docker_image(trick_data['trick'][0]['path'], container_name)
    os.chdir(original_directory)

    container = run_docker_container(
        container_name, 
        container_name,
        str(trick_data['docker_config'][0]['network_mode']), 
        trick_data['docker_config'][1]['read_only'],
        list(trick_data['docker_config'][2]['security_opt']),
        trick_data['docker_config'][3]['pid_mode'],
        trick_data['docker_config'][4]['cpu_shares'],
        trick_data['docker_config'][5]['volumes'],
        trick_data['docker_config'][6]['mem_limit'],
        trick_data['docker_config'][7]['cpuset_cpus'],
        trick_data['docker_config'][8]['cpu_quota'],
        trick_data['docker_config'][9]['cpu_period'],
        trick_data['docker_config'][10]['cap_add'],
        trick_data['docker_config'][11]['cap_drop'],
        trick_data['docker_config'][12]['privileged'],
        trick_data['docker_config'][13]['user'],
        trick_data['docker_config'][14]['pids_limit'],
        trick_data['docker_config'][15]['ipc_mode'],
        trick_data['trick'][0]['path']
    )

    # run_command_in_container(container, "ls")
