# Use the official Python image
FROM python:3.12

# Create and set up the working directory
WORKDIR /

# Create a virtual environment and install packages
RUN python -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install requests

# Specify the default command (you can override this when running the container)
CMD ["tail", "-f", "/dev/null"]
