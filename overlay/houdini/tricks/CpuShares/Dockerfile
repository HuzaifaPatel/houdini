# Use the official full Debian image
FROM debian:bookworm

# Set up the working directory
WORKDIR /

# Create a writable temporary directory and set TMPDIR
RUN mkdir -p /var/tmp && \
    export TMPDIR=/var/tmp && \
    apt-get update && \
    # Install sudo, perf, stress, bc, python3-venv, and other required system packages
    apt-get install -y sudo linux-perf procps python3 python3-pip python3-venv stress bc \
    # Install dependencies for matplotlib
    libfreetype6-dev libpng-dev libjpeg-dev libopenjp2-7 libtiff5-dev \
    gcc g++ libffi-dev libssl-dev python3-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Copy the CPU shares shell script into the container
COPY cpu_shares.sh /cpu_shares.sh

# Make the shell script executable
RUN chmod +x /cpu_shares.sh

HEALTHCHECK CMD pgrep stress || exit 1

# Step 3: Specify the command to activate the virtual environment and run the shell script
CMD ["/bin/bash", "-c", "/cpu_shares.sh"]
