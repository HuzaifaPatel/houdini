#!/bin/bash

# Check if the kernel version argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <kernel_version>"
    exit 1
fi

# Define the destination directory
DEST_DIR="../cache/kernels/$1"

exec 2>/dev/null # trash all stderr bytes
cd $PWD/buildroot/

# Save the current directory and move to the parent directory
pushd ..

sudo python3 parse_kernel_version.py 

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Return to the original directory (buildroot dir)
popd

sudo make linux-headers-dirclean
sudo make clean
sudo make > /dev/tty

# move the entire build to cache
cp -r output "$DEST_DIR/"