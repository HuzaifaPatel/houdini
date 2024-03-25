import yaml
import re

def get_major_minor_version(version_str):
    match = re.match(r"^(\d+\.\d+)", version_str)
    if match:
        return match.group(1).replace('.', '_')  # Replace dot with underscore for .config format
    return None

# Load kernel version from the YAML file
yaml_file_path = 'config/config.yml'
with open(yaml_file_path, 'r') as file:
    config_data = yaml.safe_load(file)

kernel_version = None
for item in config_data['config_lines']:
    if 'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE' in item:
        full_version = item.split('=')[1].replace('"', '').strip()
        kernel_version = get_major_minor_version(full_version)
        break

if not kernel_version:
    print("Kernel version not found in the YAML file.")
    exit()

# Modify the .config file based on the extracted version
config_file_path = 'buildroot/.config'
with open(config_file_path, 'r') as file:
    lines = file.readlines()

with open(config_file_path, 'w') as file:
    for line in lines:
        if "BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_" in line:
            # Get the version from the line and format it
            version_in_line = '_'.join(line.split('=')[0].split('_')[-2:]).strip('\n').split(" ")[0]
            if version_in_line == kernel_version:
                # If the version matches, set it to 'y'
                file.write(f"BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_{version_in_line}=y\n")
            else:
                # If it doesn't match, set it to 'is not set'
                file.write(f"# BR2_PACKAGE_HOST_LINUX_HEADERS_CUSTOM_{version_in_line} is not set\n")
        else:
            file.write(line)