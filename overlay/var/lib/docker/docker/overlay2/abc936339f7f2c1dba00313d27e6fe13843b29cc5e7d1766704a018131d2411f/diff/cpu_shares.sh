#!/bin/bash
# docker run --privileged --net=host --pid=host --cap-add=SYS_ADMIN --cap-add=CAP_SYS_PTRACE --cap-add=CAP_PERFMON --cap-add=CAP_SYSLOG --security-opt seccomp=unconfined --volume /sys:/sys --volume /tmp:/tmp -it -v ~/Desktop:/mnt/host_desktop fec02a968aa7 /bin/bash
# Step 1: Run a CPU-intensive task using the 'stress' tool
echo "Starting CPU stress test with 4 CPU workers for 60 seconds..."
stress --cpu 20 --timeout 60 &
STRESS_PID=$!

source venv/bin/activate

python3 cpu_shares.py

mv cpu_usage_chart.png /mnt/mnt