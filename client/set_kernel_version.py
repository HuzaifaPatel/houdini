import os
import subprocess
from root import get_root_dir
from config import *
import re
import fileinput

def set_br2_linux_kernel_custom_version_value(kernel_version=KERNEL_VERSION):

	for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
	    if line.startswith('BR2_LINUX_KERNEL_VERSION='):
	        line = re.sub(r'BR2_LINUX_KERNEL_VERSION=".+?"', f'BR2_LINUX_KERNEL_VERSION="{kernel_version}"', line)
	    elif line.startswith('BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE='):
	        line = re.sub(r'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE=".+?"', f'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE="{kernel_version}"', line)
	    print(line, end='')

def set_br2_package_host_linux_headers_custom(kernel_version=KERNEL_VERSION):
	major_minor_kernel_version = get_major_minor_version(kernel_version)

	for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
		if line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version) or line.startswith('# BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version):
			print('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version + "=y")
		elif line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_'):
			print("# " + line[:-3] + " is not set" + '')
		else:
			print(line, end='')

def set_br2_toolchain_headers_at_least(kernel_version=KERNEL_VERSION):
	major_minor_kernel_version = get_major_minor_version(kernel_version)

	for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
		if line.startswith('BR2_TOOLCHAIN_HEADERS_AT_LEAST'):
			# print("BR2_TOOLCHAIN_HEADERS_AT_LEAST=" + major_minor_kernel_version)
			continue
		else:
			print(line, end='')

	generate_headers_list()

def generate_headers_list(kernel_version=KERNEL_VERSION):
	default_headers = [
	    "3_0", "3_1", "3_2", "3_3", "3_4", "3_5", "3_6", "3_7", "3_8", "3_9", "3_10",
	    "3_11", "3_12", "3_13", "3_14", "3_15", "3_16", "3_17", "3_18", "3_19",
	    "4_0", "4_1", "4_2", "4_3", "4_4", "4_5", "4_6", "4_7", "4_8", "4_9", "4_10",
	    "4_11", "4_12", "4_13", "4_14", "4_15", "4_16", "4_17", "4_18", "4_19", "4_20",
	    "5_0", "5_1", "5_2", "5_3", "5_4", "5_5", "5_6", "5_7", "5_8", "5_9", "5_10",
	    "5_11", "5_12", "5_13", "5_14", "5_15", "5_16", "5_17", "5_18", "5_19",
	    "6_0", "6_1", "6_2", "6_3", "6_4"
	]

	# Convert kernel_version to major and minor parts
	major_minor_kernel_version = get_major_minor_version(kernel_version)
	major_minor_kernel_version_decimal = major_minor_kernel_version.replace('_','.')

	for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
		if line.startswith('BR2_TARGET_LDFLAGS='):
			print(line, end='')
			
			for header in default_headers:
				if compare_versions(header.replace("_", "."), major_minor_kernel_version_decimal):
					print("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y")
				elif header.replace("_", ".") == major_minor_kernel_version_decimal:
					print("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y")
					print('BR2_TOOLCHAIN_HEADERS_AT_LEAST="' + major_minor_kernel_version_decimal)
		else:
			print(line, end='')

def get_major_minor_version(kernel_version=KERNEL_VERSION):
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