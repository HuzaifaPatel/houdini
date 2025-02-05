# Use the official Ubuntu image
FROM ubuntu:22.04

# Install Python 3 and necessary packages
RUN apt-get update && \
    apt-get install -y 

# Create and set up the working directory
WORKDIR /

# Create a non-root user
RUN useradd -m myuser

# Set the user
USER myuser

# Copy the Python script into the container
COPY process_namespace.sh /process_namespace.sh

# Specify the default command (you can override this when running the container)
CMD ["/bin/bash", "/process_namespace.sh"]