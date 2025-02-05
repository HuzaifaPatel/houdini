#!/bin/bash

# Find the PID of 'python3 server.py'
PID=$(ps aux | grep '/usr/bin/python3 /houdini/server.py' | awk '{print $2}' | head -n 1)

# Check if PID exists
if [[ -n "$PID" ]]; then
    echo "Found host process python3 server.py (PID: $PID)"

    # Kill the process with SIGKILL
    echo "Killing process python3 server.py (PID: $PID) with SIGKILL..."
    kill -9 "$PID"

    # Verify if process was killed
    sleep 1
    if ps -p $PID > /dev/null; then
        echo "Failed to kill process $PID."
    else
        echo "Process $PID successfully killed."
    fi
else
    echo "Could not kill process. No process found for python3 server.py."
fi