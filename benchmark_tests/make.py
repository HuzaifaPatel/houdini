import subprocess
import psutil
import time

def run_buildroot_make():
    proc = subprocess.Popen(["make", "-C", "/path/to/buildroot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_proc = psutil.Process(proc.pid)

    wall_start = time.time()
    cpu_time_accum = 0.0

    try:
        while proc.poll() is None:
            time.sleep(1)  # poll every second
            try:
                children = ps_proc.children(recursive=True)
                cpu_time_accum += sum((c.cpu_times().user + c.cpu_times().system) for c in children if c.is_running())
            except psutil.NoSuchProcess:
                continue
    except KeyboardInterrupt:
        proc.terminate()
        print("Terminated manually.")

    wall_end = time.time()

    print(f"🧠 CPU Time (children): {cpu_time_accum:.2f} seconds")
    print(f"⏱️ Wall Time: {wall_end - wall_start:.2f} seconds")

    if proc.returncode != 0:
        print("❌ Build failed.")
    else:
        print("✅ Build succeeded.")

run_buildroot_make()
