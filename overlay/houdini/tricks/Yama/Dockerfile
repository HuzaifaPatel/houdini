FROM ubuntu:22.04

# Install required packages
RUN apt update && apt install -y python3 python3-pip gcc libc-dev

# Copy the Yama ptrace test script
COPY Yama.py /Yama.py

# Set default working directory
WORKDIR /

# Run the script by default (you can override the command to specify PID)
ENTRYPOINT ["python3", "Yama.py"]
