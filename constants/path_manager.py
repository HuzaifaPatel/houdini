import sys
import os

def get_absolute_path(extra_path = "") -> str:
	return os.path.abspath("") + extra_path

sys.path.append(get_absolute_path('/constants'))
sys.path.append(get_absolute_path('/utilities'))
sys.path.append(get_absolute_path('/config'))
sys.path.append(get_absolute_path('/api'))
sys.path.append(get_absolute_path('/kernels'))
sys.path.append(get_absolute_path('/fs'))

RUNC_MAKEFILE_PATH 			=	get_absolute_path('/buildroot/package/runc/runc.mk')
DOCKER_CLI_MAKEFILE_PATH 	= 	get_absolute_path('/buildroot/package/docker-cli/docker-cli.mk')
DOCKER_ENGINE_MAKEFILE_PATH = 	get_absolute_path('/buildroot/package/docker-engine/docker-engine.mk')
BUILDROOT_PATH 				=	get_absolute_path('/buildroot')
BUILDROOT_CONFIG_FILE 		= 	get_absolute_path('/buildroot/.config')
BUILDROOT_CUSTOM_BUILD		=	get_absolute_path('/filesystem')
KERNEL_DIR					=	get_absolute_path('/kernels')
FILESYSTEM_PATH				=	get_absolute_path('/buildroot/output')
FILESYSTEM_BUILD			=	get_absolute_path('/buildroot/output/build')