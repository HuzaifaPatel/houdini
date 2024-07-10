import os
import re
import fileinput
from houdini_config import RUNC_VERSION, DOCKER_CLI_VERSION, DOCKER_ENGINE_VERSION
from path_manager import RUNC_MAKEFILE_PATH, DOCKER_CLI_MAKEFILE_PATH, DOCKER_ENGINE_MAKEFILE_PATH, FILESYSTEM_BUILD
from style import Style

class BuildrootPackageManager:
    @staticmethod
    def modify_version(pkg_name, path, variable_to_change, pkg_version):
        if not BuildrootPackageManager.pkg_exists(pkg_name, pkg_version):
            # Use fileinput to modify the file in place
            for line in fileinput.input(path, inplace=True):
                line = re.sub(rf"{variable_to_change}\s*=\s*\S+", f"{variable_to_change} = {pkg_version}", line)
                print(line, end='')
            Style.print_color(f"Downloading {variable_to_change.replace('_', ' ')}: {pkg_version}", 'green')

    @staticmethod
    def pkg_exists(pkg_name, pkg_version) -> bool:
        pkg_folders = [name for name in os.listdir(FILESYSTEM_BUILD) if os.path.isdir(os.path.join(FILESYSTEM_BUILD, name)) and name.startswith(pkg_name)]
        
        for pkg_folder in pkg_folders:
            if pkg_folder == (pkg_name + '-' + pkg_version):
                Style.print_color(f'already downloaded: {pkg_name}-{pkg_version}', 'green')
                return True
            else:
                os.system(f"rm -rf {os.path.join(FILESYSTEM_BUILD, pkg_folder)}")
        return False

    @staticmethod
    def set_runc_version():
        BuildrootPackageManager.modify_version('runc', RUNC_MAKEFILE_PATH, "RUNC_VERSION", RUNC_VERSION)