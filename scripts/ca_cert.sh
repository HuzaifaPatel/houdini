#!/bin/sh

# Create the target directory if it doesn't exist
mkdir -p $TARGET_DIR/etc/ssl/certs

# Download CA certificates directly to the intended folder
wget https://curl.se/ca/cacert.pem -O $TARGET_DIR/etc/ssl/certs/ca-certificates.crt
