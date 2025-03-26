# Use the official Ubuntu image
FROM ubuntu:22.04

# Install Python 3 and necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Create and set up the working directory
WORKDIR /

# Create a virtual environment and install packages
RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip

# Copy the Python script into the container
COPY read_only_filesystem.py /read_only_filesystem.py

# Specify the default command (you can override this when running the container)
CMD ["venv/bin/python", "/read_only_filesystem.py"]