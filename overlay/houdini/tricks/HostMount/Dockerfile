FROM ubuntu:20.04

# Install dependencies for Python and venv
RUN apt-get update -y && apt-get install -y \
    python3 python3-pip python3-venv netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create the virtual environment in an absolute path
RUN python3 -m venv /venv && /venv/bin/pip install --upgrade pip

# Set the working directory
WORKDIR /proc/self/fd/9

# Copy the script
COPY host_mount.py /host_mount.py

# Use Python from the virtual environment
CMD ["/venv/bin/python3", "/host_mount.py"]
