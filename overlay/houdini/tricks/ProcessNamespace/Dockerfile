# Use the official Ubuntu image
FROM ubuntu:20.04

# Install Python 3 and necessary packages
RUN apt-get update && \
    apt-get install -y python3

# Create and set up the working directory
WORKDIR /

# Create a non-root user
RUN useradd -m myuser

# Copy the Python script into the container
COPY process_namespace.sh /process_namespace.sh

# Make the script executable
RUN chmod +x /process_namespace.sh

# Set the user
USER myuser

# Specify the default command (you can override this when running the container)
CMD ["/bin/bash", "/process_namespace.sh"]
