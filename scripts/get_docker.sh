#!/bin/bash

get_parent_dir() {
    echo "$(dirname "$(pwd)")"
}

python_script=$(get_parent_dir)/constants/houdini_config.py

docker_cli_version=$(python3 - <<END
import re
with open('$python_script', 'r') as f:
    content = f.read()
    match = re.search(r'DOCKER_CLI_VERSION\s*=\s*"([^"]+)"', content)
    if match:
        print(match.group(1))
END
)

# Check if the folder exists
extracted_folder="$(get_parent_dir)/misc/extracted_docker_engines/docker-${docker_cli_version}.tgz"

if [ -d "${extracted_folder}" ]; then
    echo "Found extracted folder for docker-${docker_cli_version}.tgz"

    # Copy files to overlay/bin
    cp -r "${extracted_folder}/docker/"* "$(get_parent_dir)/overlay/usr/bin/"
    echo "Copied files to $(get_parent_dir)/overlay/usr/bin/"
else
    echo "Extracted folder for docker-${docker_cli_version}.tgz not found"
fi