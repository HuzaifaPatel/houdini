# Use the official Python image (already includes Python and pip)
FROM python:3.9-slim

# Set the working directory
WORKDIR /

# Copy the Python script into the container
COPY privileged_ports.py /privileged_ports.py

# Specify the default command to run the script
CMD ["python", "privileged_ports.py"]
