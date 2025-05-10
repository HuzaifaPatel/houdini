# Use the official Ubuntu image
FROM ubuntu:14.04

# Install Python 3, hexdump (via bsdmainutils), strace, capsh (via libcap2-bin), and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 bsdmainutils strace libcap2-bin && \
    setcap cap_sys_ptrace+ep /usr/bin/strace && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and set up the working directory
WORKDIR /

# Create a non-root user
RUN useradd -m huzi

# Copy the script into the container
COPY process_namespace.sh /process_namespace.sh

# Make the script executable
RUN chmod +x /process_namespace.sh

# Specify the default command
CMD ["/bin/bash", "/process_namespace.sh"]
