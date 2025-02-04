#!/bin/bash

# Paths to overlayfs/houdini and target/houdini
overlayfs_dir="../overlay/houdini"
target_dir="../buildroot/output/target"


# List of files to remove with full paths
files=(
    "$target_dir/usr/bin/containerd"
    "$target_dir/usr/bin/containerd-shim"
    "$target_dir/usr/bin/ctr"
    "$target_dir/usr/bin/docker"
    "$target_dir/usr/bin/dockerd"
    "$target_dir/usr/bin/docker-init"
    "$target_dir/usr/bin/docker-proxy"
    "$target_dir/usr/bin/runc"
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
rsync -av "../overlay/usr/bin/" "$target_dir/usr/bin/"
rsync -av "../overlay/etc/selinux/" "$target_dir/etc/selinux/"
rsync -av --delete "../overlay/etc/inittab" "$target_dir/etc/inittab"