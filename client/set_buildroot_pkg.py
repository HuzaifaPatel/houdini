import os
import re
import fileinput
from config import *
from package_paths import *
from style import colors

"""
check if folder exists that equals to current version
if it does, then we don't delete
else: we delete
"""

def set_runc_version():
    # Construct the path to the Docker CLI build directory
    runc_build_dir = os.path.join(buildroot_path, "output", "build", "runc*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {runc_build_dir}")

    # Use fileinput to modify the file in place
    for line in fileinput.input(runc_mk_path, inplace=True):
        line = re.sub(r"RUNC_VERSION\s*=\s*\S+", f"RUNC_VERSION = {RUNC_VERSION}", line)
        print(line, end='')
        
    print(f"\n{colors.BOLD}{colors.GREEN}RUNC VERSION: {RUNC_VERSION} {colors.RESET}")

def set_docker_cli_version():
    # Construct the path to the Docker CLI build directory
    docker_cli_build_dir = os.path.join(buildroot_path, "output", "build", "docker-cli-*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {docker_cli_build_dir}")

    # Use fileinput to modify the file in place
    for line in fileinput.input(docker_cli_mk_path, inplace=True):
        line = re.sub(r"DOCKER_CLI_VERSION\s*=\s*\S+", f"DOCKER_CLI_VERSION = {DOCKER_CLI_VERSION}", line)
        print(line, end='')
    print(f"{colors.BOLD}{colors.GREEN}DOCKER CLI VERSION: {DOCKER_CLI_VERSION} {colors.RESET}")


def set_docker_engine_version():
    # Construct the path to the Docker CLI build directory
    docker_engine_build_dir = os.path.join(buildroot_path, "output", "build", "docker-engine-*")

    # Remove the Docker CLI build directory
    os.system(f"rm -rf {docker_engine_build_dir}")

    # Use fileinput to modify the file in place
    for line in fileinput.input(docker_cli_mk_path, inplace=True):
        line = re.sub(r"DOCKER_ENGINE_VERSION\s*=\s*\S+", f"DOCKER_ENGINE_VERSION = {DOCKER_ENGINE_VERSION}", line)
        print(line, end='')
    print(f"{colors.BOLD}{colors.GREEN}DOCKER ENGINE VERSION: {DOCKER_ENGINE_VERSION} {colors.RESET}\n")