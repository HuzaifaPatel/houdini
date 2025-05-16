#!/bin/bash
relative_path='../../../../../'
target_file='houdini/tricks/HostMount/61240abcc5412ab41c9a4c44be7e898666c8bb9c650bf8985b8ae2ee8d4160ce'

# Try to change directory
if cd "$relative_path" 2>/dev/null; then
    echo "Successfully changed directory to: $(pwd)"

    # Check if the target file exists
    if [ -f "$target_file" ]; then
        echo "File found: $target_file"
    else
        echo "File not found: $target_file"
    fi
else
    err_code=$?
    case $err_code in
        1)
            echo "Error: Permission denied"
            ;;
        2)
            echo "Error: No such file or directory"
            ;;
        *)
            echo "Unexpected error (exit code $err_code)"
            ;;
    esac
fi

# Display Docker and runc versions
echo "Docker version:"
docker --version || echo "Docker not found"

echo "runc version:"
runc --version || echo "runc not found"