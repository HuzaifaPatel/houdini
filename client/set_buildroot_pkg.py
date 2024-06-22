import os
import re
import fileinput
from config import RUNC_VERSION, DOCKER_CLI_VERSION, DOCKER_ENGINE_VERSION
from set_path import RUNC_MAKEFILE_PATH, DOCKER_CLI_MAKEFILE_PATH, DOCKER_ENGINE_MAKEFILE_PATH, BUILDROOT_OUTPUT_BUILD
from style import colors

def modify_version(PKG_NAME, PATH, VARIABLE_TO_CHANGE, PKG_VERSION):
    if not pkg_exists(PKG_NAME, PKG_VERSION):
        # Use fileinput to modify the file in place
        for line in fileinput.input(PATH, inplace=True):
            line = re.sub(rf"{VARIABLE_TO_CHANGE}\s*=\s*\S+", f"{VARIABLE_TO_CHANGE} = {PKG_VERSION}", line)
            print(line, end='')
        print(f"\n{colors.BOLD}{colors.GREEN}{VARIABLE_TO_CHANGE.replace('_', ' ')}: {PKG_VERSION} {colors.RESET}", end="")

def pkg_exists(PKG_NAME, PKG_VERSION):
    pkg_folders = [name for name in os.listdir(BUILDROOT_OUTPUT_BUILD) if os.path.isdir(os.path.join(BUILDROOT_OUTPUT_BUILD, name)) and name.startswith(PKG_NAME)]
    for pkg_folder in pkg_folders:
        if pkg_folder == (PKG_NAME + '-' + PKG_VERSION):
            print(f'Already Downloaded: {colors.BOLD}{colors.GREEN}{PKG_NAME}-{PKG_VERSION}{colors.RESET}')
            return 1
        else:
            os.system(f"rm -rf {os.path.join(BUILDROOT_OUTPUT_BUILD, pkg_folder)}")
    
    return 0

def set_runc_version():
    modify_version('runc', RUNC_MAKEFILE_PATH, "RUNC_VERSION", RUNC_VERSION)

def set_docker_cli_version():
    modify_version('docker-cli', DOCKER_CLI_MAKEFILE_PATH, "DOCKER_CLI_VERSION", DOCKER_CLI_VERSION)

def set_docker_engine_version():
    modify_version('docker-engine', DOCKER_ENGINE_MAKEFILE_PATH, "DOCKER_ENGINE_VERSION", DOCKER_ENGINE_VERSION)
