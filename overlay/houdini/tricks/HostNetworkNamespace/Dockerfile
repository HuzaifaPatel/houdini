# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Create and set up the working directory
WORKDIR /

# Upgrade pip and install the requests package
RUN pip install requests

# Copy the Python script into the container
COPY host_network_namespace.py /host_network_namespace.py

# Specify the default command (you can override this when running the container)
CMD ["python", "/host_network_namespace.py"]
