import re
import os
from set_kernel_version import set_br2_linux_kernel_custom_version_value, set_br2_package_host_linux_headers_custom, set_br2_toolchain_headers_at_least, generate_headers_list
from root import get_root_dir
custom_config_file = get_root_dir('/config/config.conf')

def get_requested_kernel_version():
	with open(custom_config_file, 'r') as config_file:
		match = re.search(r"KERNEL_VERSION\s*=\s*(\S+)", config_file.read())
		return match.group(1)


set_br2_linux_kernel_custom_version_value(get_requested_kernel_version())
set_br2_package_host_linux_headers_custom(get_requested_kernel_version())
set_br2_toolchain_headers_at_least(get_requested_kernel_version())
generate_headers_list(get_requested_kernel_version())