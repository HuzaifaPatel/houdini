#!/bin/bash

echo "🔪 Killing any old QEMU VMs..."
pkill -f qemu-system-x86_64 2>/dev/null || true

# Kernel and Docker versions
kernel_versions=(
6.0
6.1
6.2
6.3
6.4
6.5
6.6
6.7
)

docker_versions=(
17.03.0-ce
17.03.1-ce
17.03.2-ce
17.06.0-ce
17.06.1-ce
17.06.2-ce
17.09.0-ce
17.09.1-ce
17.12.0-ce
17.12.1-ce
18.03.0-ce
18.03.1-ce
# 18.06.0-ce
# 18.06.1-ce
# 18.06.2-ce
# 18.06.3-ce
# 18.09.0
# 18.09.1
# 18.09.2
# 18.09.3
# 18.09.4
# 18.09.5
# 18.09.6
# 18.09.7
# 18.09.8
18.09.9
19.03.0
19.03.10
19.03.11
19.03.12
19.03.13
19.03.14
19.03.15
19.03.1
19.03.2
19.03.3
19.03.4
19.03.5
19.03.6
19.03.7
19.03.8
19.03.9
20.10.0
20.10.1
20.10.2
20.10.3
)

runc_versions=(
# 1.0.0
# 1.0.0-rc10
# 1.0.0-rc2
1.0.0-rc3
# 1.0.0-rc4
# 1.0.0-rc5
# 1.0.0-rc6
# 1.0.0-rc7
# 1.0.0-rc8
# 1.0.0-rc9
# 1.0.0-rc90
# 1.0.0-rc91
# 1.0.0-rc92
# 1.0.0-rc93
# 1.0.0-rc94
# 1.0.0-rc95
# 1.0.1
# 1.0.2
# 1.0.3
# 1.1.0
# 1.1.0-rc.1
# 1.1.1
# 1.1.10
# 1.1.11
# 1.1.12
# 1.1.13
# 1.1.14
# 1.1.15
# 1.1.2
# 1.1.3
# 1.1.4
# 1.1.5
# 1.1.6
# 1.1.7
# 1.1.8
# 1.1.9
# 1.2.0
# 1.2.0-rc.1
# 1.2.0-rc.2
# 1.2.0-rc.3
# 1.2.1
# 1.2.2
# 1.2.3
# 1.2.4
# 1.2.5
# 1.2.6
# 1.3.0-rc.1
)


test_with_docker_and_kernel() {
    # Config file to modify
    local PYTHON_FILE="constants/houdini_config.py"
    local LOG_DIR="./vm_logs"

    # Define kernel and docker versions
    local kernel_versions=("5.10.0" "5.15.0")
    local docker_versions=("19.03.6" "20.10.7")

    # Create log directory
    mkdir -p "$LOG_DIR"

    for kernel_version in "${kernel_versions[@]}"; do 
        for docker_version in "${docker_versions[@]}"; do

            local LOG_FILE="${LOG_DIR}/kernel_${kernel_version}_docker_${docker_version}.log"

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

            echo "🚀 Starting VM..."
            ./houdini --start_vm > /dev/null 2>&1 &
            local VM_PID=$!

            sleep 20

            echo "📋 Getting Docker/runc versions..."
            ./houdini --get_versions >> "$LOG_FILE" 2>&1

            echo "🎯 Running trick 'host_mount'"
            ./houdini --run_trick host_mount >> "$LOG_FILE" 2>&1

            sleep 30

            # Check if VM is still running
            if kill -0 "$VM_PID" 2>/dev/null; then
                echo "🛑 Stopping VM (PID: $VM_PID)"
                kill "$VM_PID"
                wait "$VM_PID" 2>/dev/null
            else
                echo "⚠️  VM already exited (PID: $VM_PID)"
            fi

            echo "🔪 Killing any old QEMU VMs..."
            pkill -f qemu-system-x86_64 2>/dev/null || true
            sleep 3

            echo "✅ Done with Kernel $kernel_version, Docker $docker_version"
            echo "---------------------------------------------"

        done
    done
}



test_with_docker_and_runc() {
    # Config file to modify
    local PYTHON_FILE="constants/houdini_config.py"
    local LOG_DIR="./vm_logs"

    # Create log directory
    mkdir -p "$LOG_DIR"

    for docker_version in "${docker_versions[@]}"; do
        for runc_version in "${runc_versions[@]}"; do

            local LOG_FILE="${LOG_DIR}/docker_${docker_version}_runc_${runc_version}.log"

            if [ -f "$LOG_FILE" ]; then
                echo "⏭️  Skipping Docker $docker_version + Runc $runc_version — log already exists"
                continue
            fi

            echo "🔧 Updating config: Docker $docker_version, Runc $runc_version"
            sed -i "s/^DOCKER_ENGINE_VERSION = \".*\"/DOCKER_ENGINE_VERSION = \"$docker_version\"/" "$PYTHON_FILE"
            sed -i "s/^RUNC_VERSION = \".*\"/RUNC_VERSION = \"$runc_version\"/" "$PYTHON_FILE"

            echo "🛠️  Running ./houdini --mkfs (output not logged)..."
            ./houdini --mkfs > /dev/null 2>&1
            sleep 20

            echo "🚀 Starting VM..."
            ./houdini --start_vm > /dev/null 2>&1 &
            local VM_PID=$!

            sleep 20

            echo "📋 Getting Docker/runc versions..."
            ./houdini --get_versions >> "$LOG_FILE" 2>&1

            echo "🎯 Running trick 'host_mount'"
            ./houdini --run_trick host_mount >> "$LOG_FILE" 2>&1

            sleep 30

            if kill -0 "$VM_PID" 2>/dev/null; then
                echo "🛑 Stopping VM (PID: $VM_PID)"
                kill "$VM_PID"
                wait "$VM_PID" 2>/dev/null
            else
                echo "⚠️  VM already exited (PID: $VM_PID)"
            fi

            echo "🔪 Killing any old QEMU VMs..."
            pkill -f qemu-system-x86_64 2>/dev/null || true
            sleep 3

            echo "✅ Done with Docker $docker_version + Runc $runc_version"
            echo "---------------------------------------------"

        done
    done
}



test_with_docker_and_runc