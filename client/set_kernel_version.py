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

	major_minor_kernel_version = get_major_minor_version(kernel_version)
	new_lines = []
	found_custom_kernel_header = False

	for line in lines:
		if line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version) or line.startswith('# BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version):
			new_lines.append('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version + "=y\n")
			found_custom_kernel_header = True
			continue
		elif line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_'):
			new_lines.append("# " + line[:-3] + " is not set" + '\n')
		else:
			new_lines.append(line)

	# Write the modified config file back
	with open(buildroot_config_file, 'w') as file:
		file.writelines(new_lines)

def set_br2_toolchain_headers_at_least(kernel_version):
	with open(buildroot_config_file, 'r') as file:
		lines = file.readlines()

	major_minor_kernel_version = get_major_minor_version(kernel_version)
	new_lines = []
	found_toolchain_headers = False

	for line in lines:
		if line.startswith('BR2_TOOLCHAIN_HEADERS_AT_LEAST'):
			new_lines.append("BR2_TOOLCHAIN_HEADERS_AT_LEAST=" + major_minor_kernel_version)
		else:
			new_lines.append(line)

	# Write the modified config file back
	with open(buildroot_config_file, 'w') as file:
		file.writelines(new_lines)


def generate_headers_list(kernel_version):
	default_headers = [
	    "3_0", "3_1", "3_2", "3_3", "3_4", "3_5", "3_6", "3_7", "3_8", "3_9", "3_10",
	    "3_11", "3_12", "3_13", "3_14", "3_15", "3_16", "3_17", "3_18", "3_19",
	    "4_0", "4_1", "4_2", "4_3", "4_4", "4_5", "4_6", "4_7", "4_8", "4_9", "4_10",
	    "4_11", "4_12", "4_13", "4_14", "4_15", "4_16", "4_17", "4_18", "4_19", "4_20",
	    "5_0", "5_1", "5_2", "5_3", "5_4", "5_5", "5_6", "5_7", "5_8", "5_9", "5_10",
	    "5_11", "5_12", "5_13", "5_14", "5_15", "5_16", "5_17", "5_18", "5_19",
	    "6_0", "6_1", "6_2", "6_3", "6_4"
	]

	with open(buildroot_config_file, 'r') as file:
		lines = file.readlines()

	new_headers = []
	new_lines = []

	# Convert kernel_version to major and minor parts
	major_minor_kernel_version = get_major_minor_version(kernel_version)
	major_minor_kernel_version_decimal = major_minor_kernel_version.replace('_','.')

	for header in default_headers:
		if compare_versions(header.replace("_", "."), major_minor_kernel_version_decimal):
			new_headers.append("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y\n")
		elif header.replace("_", ".") == major_minor_kernel_version_decimal:
			new_headers.append("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y\n")
			new_headers.append('BR2_TOOLCHAIN_HEADERS_AT_LEAST="' + major_minor_kernel_version_decimal + '"\n')

	found_headers = False

	for line in lines:
		if line.startswith('BR2_TARGET_LDFLAGS='):
			found_headers = True
			new_lines.append(line)
			continue
		elif found_headers:
			for header in new_headers:
				new_lines.append(header)
			found_headers = False
		else:
			new_lines.append(line)


	# Write the modified config file back
	with open(buildroot_config_file, 'w') as file:
		file.writelines(new_lines)


def get_major_minor_version(kernel_version):
    # Split the version string by the dot to separate major, minor, and patch versions
    version_parts = kernel_version.split('.')

    # Extract the major and minor versions
    major_version = version_parts[0]
    minor_version = version_parts[1] if len(version_parts) > 1 else '0'

    # Format the string as major_minor
    formatted_version = f"{major_version}_{minor_version}"

    return formatted_version


def compare_versions(kernel_version1, kernel_version2):
	def version_to_tuple(version):
		return tuple(map(int, version.split('.')))
	
	return version_to_tuple(kernel_version1) < version_to_tuple(kernel_version2)