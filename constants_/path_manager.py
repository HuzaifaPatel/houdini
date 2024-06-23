import sys
import os

def get_absolute_path(extra_path = "") -> str:
	return os.path.abspath("") + extra_path

sys.path.append(get_absolute_path('/constants_'))
sys.path.append(get_absolute_path('/client'))
sys.path.append(get_absolute_path('/config'))
sys.path.append(get_absolute_path('/api'))

RUNC_MAKEFILE_PATH 			=	get_absolute_path('/buildroot/package/runc/runc.mk')
DOCKER_CLI_MAKEFILE_PATH 	= 	get_absolute_path('/buildroot/package/docker-cli/docker-cli.mk')
DOCKER_ENGINE_MAKEFILE_PATH = 	get_absolute_path('/buildroot/package/docker-engine/docker-engine.mk')
BUILDROOT_PATH 				=	get_absolute_path('/buildroot')
BUILDROOT_CONFIG_FILE 		= 	get_absolute_path('/buildroot/.config')
BUILDROOT_OUTPUT_BUILD		= 	get_absolute_path('/buildroot/output/build')