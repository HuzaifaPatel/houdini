# Use the official Python image (already includes Python and pip)
FROM python:3.7-slim

# Create a new user and group
RUN groupadd -r huzi && useradd -r -g huzi huzi

# Set the working directory
WORKDIR /

# Copy the Python script into the container
COPY privileged_ports.py /privileged_ports.py

# Change ownership of the working directory and script to the new user
RUN chown huzi:huzi privileged_ports.py 

# Specify the default command to run the script
CMD ["python", "privileged_ports.py"]
