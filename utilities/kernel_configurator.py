import os
import subprocess
from path_manager import *
import kernel_headers
from houdini_config import KERNEL_VERSION
import re
import fileinput

class KernelConfigurator:
    
    @staticmethod
    def set_br2_linux_kernel_custom_version_value():
        for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
            if line.startswith('BR2_LINUX_KERNEL_VERSION='):
                line = re.sub(r'BR2_LINUX_KERNEL_VERSION=".+?"', f'BR2_LINUX_KERNEL_VERSION="{KERNEL_VERSION}"', line)
            elif line.startswith('BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE='):
                line = re.sub(r'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE=".+?"', f'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE="{KERNEL_VERSION}"', line)
            print(line, end='')

    @staticmethod
    def set_br2_package_host_linux_headers_custom():
        major_minor_kernel_version = KernelConfigurator.get_major_minor_version(KERNEL_VERSION)

        for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
            if line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version) or line.startswith('# BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version):
                print('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_' + major_minor_kernel_version + "=y")
            elif line.startswith('BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_'):
                print("# " + line[:-3] + " is not set" + '')
            else:
                print(line, end='')

    @staticmethod
    def set_br2_toolchain_headers_at_least():
        major_minor_kernel_version = KernelConfigurator.get_major_minor_version(KERNEL_VERSION)

        for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
            if line.startswith('BR2_TOOLCHAIN_HEADERS_AT_LEAST'):
                continue
            else:
                print(line, end='')

        KernelConfigurator.generate_headers_list()

    @staticmethod
    def set_BR2_DEFAULT_KERNEL_VERSION():
        for line in fileinput.input(FILESYSTEM_CONFIG_FILE, inplace=True):
            if line.startswith('BR2_DEFAULT_KERNEL_VERSION='):
                print(f'BR2_DEFAULT_KERNEL_VERSION="{KERNEL_VERSION}"')
            else:
                print(line, end='')  # end='' prevents print from adding an extra newline

    @staticmethod
    def generate_headers_list():
        major_minor_kernel_version = KernelConfigurator.get_major_minor_version(KERNEL_VERSION)
        major_minor_kernel_version_decimal = major_minor_kernel_version.replace('_', '.')

        for line in fileinput.input(BUILDROOT_CONFIG_FILE, inplace=True):
            if line.startswith('BR2_TARGET_LDFLAGS='):
                print(line, end='')

                for header in kernel_headers.default_headers:
                    if KernelConfigurator.compare_versions(header.replace("_", "."), major_minor_kernel_version_decimal):
                        print("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y")
                    elif header.replace("_", ".") == major_minor_kernel_version_decimal:
                        print("BR2_TOOLCHAIN_HEADERS_AT_LEAST_" + header + "=y")
                        print('BR2_TOOLCHAIN_HEADERS_AT_LEAST="' + major_minor_kernel_version_decimal)
            else:
                print(line, end='')

    @staticmethod
    def get_major_minor_version(kernel_version=KERNEL_VERSION):
        version_parts = kernel_version.split('.')
        major_version = version_parts[0]
        minor_version = version_parts[1] if len(version_parts) > 1 else '0'
        formatted_version = f"{major_version}_{minor_version}"
        return formatted_version

    @staticmethod
    def compare_versions(kernel_version1, kernel_version2):
        def version_to_tuple(version):
            return tuple(map(int, version.split('.')))
        return version_to_tuple(kernel_version1) < version_to_tuple(kernel_version2)
