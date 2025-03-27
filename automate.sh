#!/bin/bash

# Kernel and Docker versions
kernel_versions=(6.0 6.1 6.2 6.3 6.4 6.5 6.6 6.7)
docker_versions=(27.0.1 26.0.0 25.0.0 24.0.0 23.0.0 20.10.0 18.09.0)

# Config file to modify
PYTHON_FILE="constants/houdini_config.py"
LOG_DIR="./vm_logs"

# Create log directory
mkdir -p "$LOG_DIR"

for kernel_version in "${kernel_versions[@]}"; do
    for docker_version in "${docker_versions[@]}"; do

        LOG_FILE="${LOG_DIR}/kernel_${kernel_version}_docker_${docker_version}.log"

        # ✅ Skip if log already exists
        if [ -f "$LOG_FILE" ]; then
            echo "⏭️  Skipping Kernel $kernel_version, Docker $docker_version — log already exists"
            continue
        fi

        echo "🔧 Updating config: Kernel $kernel_version, Docker $docker_version"

        # Update Python config
        sed -i "s/^KERNEL_VERSION = \".*\"/KERNEL_VERSION = \"$kernel_version\"/" "$PYTHON_FILE"
        sed -i "s/^DOCKER_ENGINE_VERSION = \".*\"/DOCKER_ENGINE_VERSION = \"$docker_version\"/" "$PYTHON_FILE"

        echo "🛠️  Running ./houdini --mkfs (output not logged)..."
        ./houdini --mkfs > /dev/null 2>&1
        sleep 20

        echo "🚀 Starting VM (log: $LOG_FILE)..."
        ./houdini --start_vm >> "$LOG_FILE" 2>&1 &
        VM_PID=$!

        sleep 20

        echo "🎯 Running trick 'process_namespace'"
        ./houdini --run_trick process_namespace >> "$LOG_FILE" 2>&1

        sleep 30

        # Check if VM is still running
        if kill -0 "$VM_PID" 2>/dev/null; then
            echo "🛑 Stopping VM (PID: $VM_PID)"
            kill "$VM_PID"
            wait "$VM_PID" 2>/dev/null
        else
            echo "⚠️  VM already exited (PID: $VM_PID)"
        fi

        echo "✅ Done with Kernel $kernel_version, Docker $docker_version"
        echo "---------------------------------------------"

    done
done
