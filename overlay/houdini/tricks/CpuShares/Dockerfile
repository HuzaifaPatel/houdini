# Use the official Python slim image
FROM python:3.9-slim

# Set up the working directory
WORKDIR /

# Install Python packages directly
RUN pip install --no-cache-dir requests psutil

# Copy the Python script into the container
COPY cpu_shares.py /cpu_shares.py

# Specify the default command
CMD ["python", "/cpu_shares.py"]
