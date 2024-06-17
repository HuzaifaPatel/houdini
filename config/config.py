from root import *

RUNC_VERSION = "1.1.11"
DOCKER_CLI_VERSION = "25.0.0"
DOCKER_ENGINE_VERSION = "25.0.0"
KERNEL_VERSION = "6.3.4"
PY_CONFIG_FILE = get_root_dir('/client/config.py')
BUILDROOT_CONFIG_FILE = get_root_dir('/buildroot/.config')
PORT = 5005
VM_URL = f'http://127.0.0.1:{PORT}'