# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Create and set up the working directory
WORKDIR /


# Copy the Python script into the container
COPY pid_limit.py /pid_limit.py

# Specify the default command (you can override this when running the container)
CMD ["python", "/pid_limit.py"]
