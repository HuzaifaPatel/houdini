#!/bin/bash

PID=$(ps aux | grep '[p]ython3 /houdini/server.py' | awk '{print $2}' | head -n 1)

if [[ -n "$PID" ]]; then
    echo "Found host process python3 server.py (PID: $PID)"
else
    echo "Could not kill process. No process found for python3 server.py."
fi
