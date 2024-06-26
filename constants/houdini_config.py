RUNC_VERSION = "1.1.12"
DOCKER_CLI_VERSION = "26.0.0"
DOCKER_ENGINE_VERSION = "26.0.0"
KERNEL_VERSION = "6.5.5"
PORT = 49153
VM_URL = f'http://127.0.0.1:{PORT}'
VM_RAM = 5000
CPU_CORES = 15


def print_config():
	from style import Style
	for name, value in globals().items():
		if name.isupper() and not name.startswith('__') and not callable(value):
			Style.print_color(name, 'green', ': ')
			print(value)