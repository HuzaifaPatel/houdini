#!/bin/bash

# Paths to overlayfs/houdini and target/houdini
overlayfs_dir="../overlay/houdini"
target_dir="../buildroot/output/target/houdini"

# Synchronize overlayfs/houdini with target/houdini
rsync -av --delete "$overlayfs_dir/" "$target_dir/"