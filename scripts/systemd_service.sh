#!/bin/bash

# Get the target directory from the first argument
TARGET_DIR="$1"
SYSTEMD_DIR="${TARGET_DIR}/etc/systemd/system"
WANTS_DIR="${SYSTEMD_DIR}/multi-user.target.wants"

# Ensure the necessary directories exist
mkdir -p "${SYSTEMD_DIR}"
mkdir -p "${WANTS_DIR}"

# Create the systemd service file
cat <<EOF > "${SYSTEMD_DIR}/houdini-server.service"
[Unit]
Description=Start Houdini Server
After=network.target

[Service]
ExecStart=/bin/python3 /houdini/server.py
Restart=on-failure
RestartSec=5s
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# Ensure the service file has the correct permissions
chmod 644 "${SYSTEMD_DIR}/houdini-server.service"

# Remove any existing symbolic link to avoid duplicates
rm -f "${WANTS_DIR}/houdini-server.service"

# Create the symbolic link to enable the service
ln -sf "${SYSTEMD_DIR}/houdini-server.service" "${WANTS_DIR}/houdini-server.service"