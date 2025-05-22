#!/bin/bash

get_version_from_config() {
    local variable_name=$1
    local config_path="/home/huzi/Documents/houdini/constants/houdini_config.py"

    python3 -c "
import re
with open('$config_path', 'r') as f:
    content = f.read()
    match = re.search(r'$variable_name\s*=\s*\"([^\"]+)\"', content)
    if match:
        print(match.group(1))
" 2>/dev/null
}

remove_initd_scripts() {
    echo -e "\n🧹 Removing init.d scripts..."

    local INITD_DIR="/home/huzi/Documents/houdini/buildroot/output/target/etc/init.d"

    if [ ! -d "$INITD_DIR" ]; then
        echo "❌ Directory not found: $INITD_DIR"
        return 1
    fi

    local SCRIPTS=(
        "S50docker"
        "S99docker_login"
        "S50houdini"
        "S99http_server"
        "S99set_docker_pro"
        "S99huzi_startup"
    )

    for script in "${SCRIPTS[@]}"; do
        local filepath="$INITD_DIR/$script"
        if [ -f "$filepath" ]; then
            rm "$filepath"
            echo "🗑️  Removed $script"
        else
            echo "➖ $script not found, skipping"
        fi
    done
}

remove_docker_binaries() {
    echo -e "\n🔧 Running remove_docker_binaries..."

    local TARGET_DIR="/home/huzi/Documents/houdini/buildroot/output/target/usr/bin"
    local TARGET_DIR_OVERLAY="/home/huzi/Documents/houdini/overlay/usr/bin"

    local BINARIES=(
        "docker"
        "docker-containerd"
        "docker-containerd-ctr"
        "docker-containerd-shim"
        "dockerd"
        "docker-init"
        "docker-proxy"
        "docker-runc"
        "runc"
        "containerd"
        "ctr"
        "containerd-shim-runc-v2"
        "containerd-shim"
        "crun"
    )

    for dir in "$TARGET_DIR" "$TARGET_DIR_OVERLAY"; do
        if [ ! -d "$dir" ]; then
            echo "❌ Directory not found: $dir"
            continue
        fi

        echo "📁 Checking directory: $dir"
        for binary in "${BINARIES[@]}"; do
            if [ -f "$dir/$binary" ]; then
                rm "$dir/$binary"
                echo "🗑️  Removed $binary from $dir"
            else
                echo "➖ $binary not found in $dir, skipping"
            fi
        done
    done
}


get_docker_engine_binaries() {
    echo -e "\n🐳 Running get_docker_engine_binaries..."

    local version_file="/tmp/docker_engine_version.txt"
    get_version_from_config "DOCKER_ENGINE_VERSION" > "$version_file"
    local docker_engine_version
    docker_engine_version=$(cat "$version_file")
    rm "$version_file"

    echo "✅ Docker engine version: $docker_engine_version"

    local extracted_folder="/home/huzi/Documents/houdini/misc/extracted_docker_engines/docker-${docker_engine_version}.tgz"
    local overlay_bin="/home/huzi/Documents/houdini/overlay/usr/bin"

    if [ -d "${extracted_folder}" ]; then
        echo "📦 Found extracted folder for docker-${docker_engine_version}.tgz"
        cp -r "${extracted_folder}/docker/"* "$overlay_bin/"
        echo "📥 Copied files to $overlay_bin"
        chmod +x "$overlay_bin"/*
        echo "✅ Marked all files in $overlay_bin as executable"
    else
        echo "❌ Extracted folder for docker-${docker_engine_version}.tgz not found"
    fi
}

get_runc_binaries() {
    echo -e "\n📦 Running get_runc_binaries..."

    local version_file="/tmp/runc_version.txt"
    get_version_from_config "RUNC_VERSION" > "$version_file"
    local runc_version
    runc_version=$(cat "$version_file")
    rm "$version_file"

    echo "✅ RUNC version: $runc_version"

    local extracted_folder="/home/huzi/Documents/houdini/misc/runc/runc-${runc_version}"
    local overlay_bin="/home/huzi/Documents/houdini/overlay/usr/bin"

    if [ -d "${extracted_folder}" ]; then
        echo "📦 Found extracted folder for runc-${runc_version}"

        local src_runc="${extracted_folder}/runc"
        if [ ! -f "$src_runc" ]; then
            echo "❌ ERROR: $src_runc not found in extracted folder"
            return 1
        fi

        if [ -f "${overlay_bin}/docker-runc" ]; then
            cp "$src_runc" "${overlay_bin}/docker-runc"
            echo "📄 Copied runc as docker-runc"
        else
            cp "$src_runc" "${overlay_bin}/runc"
            echo "📄 Copied runc as runc"
        fi

        chmod +x "${overlay_bin}/runc" "${overlay_bin}/docker-runc" 2>/dev/null
        echo "✅ Marked copied file(s) as executable"
    else
        echo "❌ Extracted folder for runc-${runc_version} not found"
    fi
}


get_crun_binaries() {
    echo -e "\n📦 Running get_crun_binaries..."

    local version_file="/tmp/crun_version.txt"
    get_version_from_config "CRUN_VERSION" > "$version_file"
    local crun_version
    crun_version=$(cat "$version_file")
    rm "$version_file"

    echo "✅ CRUN version: $crun_version"

    local extracted_folder="/home/huzi/Documents/houdini/misc/crun/$crun_version"
    local overlay_bin="/home/huzi/Documents/houdini/overlay/usr/bin"

    if [ -d "${extracted_folder}" ]; then
        echo "📦 Found extracted folder for crun-${crun_version}"

        local src_crun
        src_crun=$(find "$extracted_folder" -type f -name "crun-*linux-amd64" | head -n 1)

        if [ ! -f "$src_crun" ]; then
            echo "❌ ERROR: crun binary not found in extracted folder"
            return 1
        fi

        cp "$src_crun" "${overlay_bin}/crun"
        echo "📄 Copied crun as crun"

        chmod +x "${overlay_bin}/crun" 2> /dev/null
        echo "✅ Marked copied file(s) as executable"
    else
        echo "❌ Extracted folder for crun-${crun_version} not found"
    fi
}


# ---- Execute in strict order ----
remove_docker_binaries
remove_initd_scripts
get_docker_engine_binaries
# get_runc_binaries
get_crun_binaries
