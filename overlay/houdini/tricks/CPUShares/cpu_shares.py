import time

PROCFS = "/host_proc"  # Path to the mounted /proc directory

def read_cpu_stats():
    """Read the CPU stats from /proc/stat."""
    with open(f"{PROCFS}/stat", "r") as f:
        lines = f.readlines()

    # Look for the line starting with 'cpu '
    for line in lines:
        if line.startswith("cpu "):  # The first line aggregates all CPUs
            cpu_times = line.split()[1:]
            cpu_times = list(map(int, cpu_times))
            return cpu_times
    return None

def calculate_cpu_usage(cpu_times_1, cpu_times_2):
    """Calculate the CPU usage between two readings."""
    total_time_1 = sum(cpu_times_1)
    total_time_2 = sum(cpu_times_2)
    
    idle_time_1 = cpu_times_1[3]  # idle time is the 4th value
    idle_time_2 = cpu_times_2[3]

    total_delta = total_time_2 - total_time_1
    idle_delta = idle_time_2 - idle_time_1

    usage = 100 * (total_delta - idle_delta) / total_delta
    return usage

def monitor_cpu_usage(interval=1, duration=60):
    """Monitor the CPU usage of the host in real-time."""
    print("Starting CPU usage monitoring...", flush=True)
    end_time = time.time() + duration
    while time.time() < end_time:
        cpu_times_1 = read_cpu_stats()
        time.sleep(interval)
        cpu_times_2 = read_cpu_stats()

        if cpu_times_1 and cpu_times_2:
            cpu_usage = calculate_cpu_usage(cpu_times_1, cpu_times_2)
            print(f"Host CPU Usage: {cpu_usage:.2f}%", flush=True)
        else:
            print("Failed to read CPU stats.", flush=True)
        
        time.sleep(interval)  # Wait before the next read


monitor_cpu_usage(interval=1, duration=60)  # Adjust the interval and duration as needed
	
