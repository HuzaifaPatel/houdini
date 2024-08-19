RUNC_VERSION = "1.1.11"
DOCKER_CLI_VERSION = "23.0.0"
DOCKER_ENGINE_VERSION = "23.0.0"
KERNEL_VERSION = "6.5.5"
PORT = 49153
VM_URL = f'http://127.0.0.1:{PORT}'
VM_RAM = 4000
CPU_CORES = 4
PRIV_MODE = False

#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX = "disabled"
APPARMOR = "docker-default" # not working yet

def get_value(variable_name):
    global_vars = globals()
    if variable_name in global_vars:
        return global_vars[variable_name]
    else:
        return f"Variable '{variable_name}' not found"