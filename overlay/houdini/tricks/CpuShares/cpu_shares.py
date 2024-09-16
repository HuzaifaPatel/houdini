import multiprocessing
import time
import psutil

# A CPU-intensive task to consume processing power
def cpu_stress_test():
    print(f"Starting CPU stress test in process {multiprocessing.current_process().pid}")
    while True:
        # Perform CPU-intensive calculations
        result = sum(i * i for i in range(10**6))  # Heavy computation

def monitor_cpu_usage(queue, interval=1):
    """Monitor CPU usage and put it onto the queue."""
    while True:
        usage = psutil.cpu_percent(interval=interval, percpu=True)
        queue.put(usage)  # Put the CPU usage on the queue

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get the number of CPU cores
    print(f"Spawning {num_cores} processes to stress the CPU")

    # Create a queue for inter-process communication
    queue = multiprocessing.Queue()

    # Create and start processes to stress the CPU
    processes = []
    for _ in range(num_cores):
        process = multiprocessing.Process(target=cpu_stress_test)
        process.start()
        processes.append(process)

    # Create a process to monitor CPU usage
    monitor_process = multiprocessing.Process(target=monitor_cpu_usage, args=(queue, 1))
    monitor_process.start()

    # Let the stress test run for some time (e.g., 60 seconds)
    try:
        end_time = time.time() + 60  # Run for 60 seconds
        while time.time() < end_time:
            if not queue.empty():
                usage = queue.get()
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                avg_usage = sum(usage) / len(usage)
                print(f"[{timestamp}] Host CPU Usage per core: {usage}%")
                print(f"[{timestamp}] Average CPU Usage: {avg_usage:.2f}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Terminating stress test")

    # Terminate all stress test processes
    for process in processes:
        process.terminate()

    # Terminate the CPU monitoring process
    monitor_process.terminate()
