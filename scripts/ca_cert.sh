#!/bin/sh

# Download CA certificates
wget https://curl.se/ca/cacert.pem

# Extract and install CA certificates
mkdir -p $TARGET_DIR/etc/ssl/certs
cp cacert.pem $TARGET_DIR/etc/ssl/certs/ca-certificates.crt
