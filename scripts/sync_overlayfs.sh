#!/bin/bash

# Paths to overlayfs/houdini and target/houdini
overlayfs_dir="../overlay/houdini"
target_dir="../buildroot/output/target"

# Synchronize overlayfs/houdini with target/houdini
rsync -av --delete "$overlayfs_dir" "$target_dir"
rsync -av "../overlay/usr/bin/" "$target_dir/usr/bin/"
rsync -av "../overlay/etc/selinux/" "$target_dir/etc/selinux/"
rsync -av --delete "../overlay/etc/inittab" "$target_dir/etc/inittab"