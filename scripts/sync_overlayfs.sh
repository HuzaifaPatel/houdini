#!/bin/bash

# Paths to overlayfs/houdini and target/houdini
overlayfs_dir="../overlay/houdini"
target_dir="../filesystem/target/houdini"


# List of files to remove with full paths
files=(
    "../filesystem/target/usr/bin/containerd"
    "../filesystem/target/usr/bin/containerd-shim"
    "../filesystem/target/usr/bin/ctr"
    "../filesystem/target/usr/bin/docker"
    "../filesystem/target/usr/bin/dockerd"
    "../filesystem/target/usr/bin/docker-init"
    "../filesystem/target/usr/bin/docker-proxy"
    "../filesystem/target/usr/bin/runc"
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

# Synchronize overlayfs/houdini with target/houdini
rsync -av --delete "$overlayfs_dir" "$target_dir"
rsync -av "../overlay/usr/bin/" "../filesystem/target/usr/bin/"