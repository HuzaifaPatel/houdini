import os
import subprocess
from root import get_root_dir
#do not change any other part of .config

buildroot_path = get_root_dir("/buildroot")
buildroot_config_file = get_root_dir("/buildroot/.config")
custom_config_file = get_root_dir('/config/config.conf')

# depends on br2_linux_kernel = y, br2_linux_kernel_custom_value = y
def set_br2_linux_kernel_custom_version_value(kernel_version):

	 # Set the kernel version
    # subprocess.run(f"sed -i 's/^BR2_LINUX_KERNEL_VERSION=.*/BR2_LINUX_KERNEL_VERSION=\"{kernel_version}\"/' {buildroot_config_file}", shell=True, check=True)

    # Read the config file
    with open(buildroot_config_file, 'r') as file:
        lines = file.readlines()

    # Prepare new lines
    new_lines = []
    found_kernel_version = False
    found_custom_version = False

    for line in lines:
        if line.startswith('BR2_LINUX_KERNEL_VERSION='):
            new_lines.append(f'BR2_LINUX_KERNEL_VERSION="{kernel_version}"\n')
            found_kernel_version = True
        elif line.startswith('BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE='):
            new_lines.append(f'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE="{kernel_version}"\n')
            found_custom_version = True
        else:
            new_lines.append(line)

    # Write the modified config file back
    with open(buildroot_config_file, 'w') as file:
        file.writelines(new_lines)

    # Run make olddefconfig to update the configuration
    # subprocess.run(f"make -C {buildroot_path} olddefconfig", shell=True, check=True)

def set_br2_package_host_linux_headers_custom(kernel_version):
	with open(buildroot_config_file, 'r') as file:
		lines = file.readlines()

	major_minor_kernel_version = get_major_minor_version()
	new_lines = []
	found_custom_kernel_header = False

	for line in lines:
		if line.startswith('# BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_'):
			continue
		elif line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_'):
			new_lines.append('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version + "=y")
		else:
			new_lines.append(line)

def get_major_minor_version(kernel_version):
    # Split the version string by the dot to separate major, minor, and patch versions
    version_parts = kernel_version.split('.')

    # Extract the major and minor versions
    major_version = version_parts[0]
    minor_version = version_parts[1] if len(version_parts) > 1 else '0'

    # Format the string as major_minor
    formatted_version = f"{major_version}_{minor_version}"

    return formatted_version

