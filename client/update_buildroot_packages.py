import re
import os
from root import get_root_dir
config_path = get_root_dir('/config/config.conf')
runc_mk_path = get_root_dir('/buildroot/package/runc/runc.mk')
docker_cli_mk_path = get_root_dir('/buildroot/package/docker-cli/docker-cli.mk')
docker_engine_mk_path = get_root_dir('/buildroot/package/docker-engine/docker-engine.mk')
buildroot_path = get_root_dir('../buildroot')

def update_runc_version(config_path, runc_mk_path):
    # Construct the path to the Docker CLI build directory
    runc_build_dir = os.path.join(buildroot_path, "output", "build", "runc*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {runc_build_dir}")

    # Read the desired version from config.conf
    with open(config_path, "r") as config_file:
        config_content = config_file.read()
        match = re.search(r"RUNC_VERSION\s*=\s*(\S+)", config_content)
        if match:
            runc_version = match.group(1)
        else:
            print("RUNC_VERSION not found in config.conf")
            return

    # Update the RUNC_VERSION variable in runc.mk
    with open(runc_mk_path, "r") as runc_mk_file:
        runc_mk_content = runc_mk_file.read()

    # Replace the RUNC_VERSION variable
    runc_mk_content = re.sub(r"RUNC_VERSION\s*=\s*(\S+)", f"RUNC_VERSION = {runc_version}", runc_mk_content)

    # Write the updated content back to runc.mk
    with open(runc_mk_path, "w") as runc_mk_file:
        runc_mk_file.write(runc_mk_content)

    print(f"Updated RUNC_VERSION to {runc_version} in {runc_mk_path}")

update_runc_version(config_path, runc_mk_path)

def update_docker_cli_version(config_path, docker_cli_mk_path):
    # Construct the path to the Docker CLI build directory
    docker_cli_build_dir = os.path.join(buildroot_path, "output", "build", "docker-cli-*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {docker_cli_build_dir}")

    # Read the desired version from config.conf
    with open(config_path, "r") as config_file:
        config_content = config_file.read()
        match = re.search(r"DOCKER_CLI_VERSION\s*=\s*(\S+)", config_content)
        if match:
            docker_cli_version = match.group(1)
        else:
            print("DOCKER_CLI_VERSION not found in config.conf")
            return

    # Update the DOCKER_CLI_VERSION variable in docker-cli.mk
    with open(docker_cli_mk_path, "r") as docker_cli_mk_file:
        docker_cli_mk_content = docker_cli_mk_file.read()

    # Replace the DOCKER_CLI_VERSION variable
    docker_cli_mk_content = re.sub(r"DOCKER_CLI_VERSION\s*=\s*(\S+)", f"DOCKER_CLI_VERSION = {docker_cli_version}", docker_cli_mk_content)

    # Write the updated content back to docker-cli.mk
    with open(docker_cli_mk_path, "w") as docker_cli_mk_file:
        docker_cli_mk_file.write(docker_cli_mk_content)

    print(f"Updated DOCKER_CLI_VERSION to {docker_cli_version} in {docker_cli_mk_path}")


update_docker_cli_version(config_path, docker_cli_mk_path)

def update_docker_engine_version(config_path, docker_engine_mk_path):
    # Construct the path to the Docker CLI build directory
    docker_engine_build_dir = os.path.join(buildroot_path, "output", "build", "docker-engine-*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {docker_engine_build_dir}")

    # Read the desired version from config.conf
    with open(config_path, "r") as config_file:
        config_content = config_file.read()
        match = re.search(r"DOCKER_ENGINE_VERSION\s*=\s*(\S+)", config_content)
        if match:
            docker_engine_version = match.group(1)
        else:
            print("DOCKER_ENGINE_VERSION not found in config.conf")
            return

    # Update the DOCKER_ENGINE_VERSION variable in docker-engine.mk
    with open(docker_engine_mk_path, "r") as docker_engine_mk_file:
        docker_engine_mk_content = docker_engine_mk_file.read()

    # Replace the DOCKER_ENGINE_VERSION variable
    docker_engine_mk_content = re.sub(r"DOCKER_ENGINE_VERSION\s*=\s*(\S+)", f"DOCKER_ENGINE_VERSION = {docker_engine_version}", docker_engine_mk_content)

    # Write the updated content back to docker-engine.mk
    with open(docker_engine_mk_path, "w") as docker_engine_mk_file:
        docker_engine_mk_file.write(docker_engine_mk_content)

    print(f"Updated DOCKER_ENGINE_VERSION to {docker_engine_version} in {docker_engine_mk_path}")

update_docker_engine_version(config_path, docker_engine_mk_path)