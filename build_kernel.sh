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

# sudo make linux-headers-dirclean
# sudo make clean
sudo make > /dev/tty

# Check if the destination directory does not exist
if [ ! -d "$DEST_DIR" ]; then
    # Destination directory does not exist, so copy the output directory
    cp -r output "$DEST_DIR/"
    echo "Output directory copied to $DEST_DIR"
else
    # Destination directory exists, so do not copy
    echo "$DEST_DIR already exists. Copy not performed."
fi