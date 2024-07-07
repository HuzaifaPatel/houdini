#!/bin/bash

# Paths to overlayfs/houdini and target/houdini
overlayfs_dir="../overlay/houdini"
target_dir="output/target/houdini"

# Synchronize overlayfs/houdini with target/houdini
rsync -av --delete "$overlayfs_dir/" "$target_dir/"

echo $PWD
# List of files to remove with full paths
files=(
    ".output/target/usr/bin/containerd"
    ".output/target/usr/bin/containerd-shim"
    ".output/target/usr/bin/ctr"
    ".output/target/usr/bin/docker"
    ".output/target/usr/bin/dockerd"
    ".output/target/usr/bin/docker-init"
    ".output/target/usr/bin/docker-proxy"
    ".output/target/usr/bin/runc"
)

# Loop through each file and remove it
for file in "${files[@]}"; do
    if [ -f "$file" ]; then  # Check if file exists before attempting to remove
        rm -f "$file"
        echo "Removed: $file"
    else
        echo "File does not exist: $file"
    fi
done