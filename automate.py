import subprocess
import itertools
import re
import sys
import socket
import time
import importlib
# import psutil
import os

# parent = psutil.Process() 
sys.path.append('constants')
sys.path.append('trick_configs')
from houdini_config import *

CONFIG_PATH = "constants/houdini_config.py"
LOG_DIR = "logs"

MAX_TESTS = 32

def ensure_log_dir():
    os.makedirs(LOG_DIR, exist_ok=True)

def update_docker_engine_version(version):
    with open(CONFIG_PATH, "r") as f:
        lines = f.readlines()
    with open(CONFIG_PATH, "w") as f:
        for line in lines:
            if line.strip().startswith("DOCKER_ENGINE_VERSION"):
                f.write(f'DOCKER_ENGINE_VERSION = "{version}"\n')
            else:
                f.write(line)

def mkfs():
    subprocess.run(["./houdini", "--mkfs"], check=True)

def start_vm():
    subprocess.run(["./houdini", "--start_vm"], check=True)

def wait_for_port(host="127.0.0.1", port=49153, timeout=50):
    print(f"Waiting for VM to open port {port}...")
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            if sock.connect_ex((host, port)) == 0:
                print("VM port is open and ready.")
                return
        time.sleep(1)
    raise TimeoutError(f"VM port {port} did not become ready in {timeout} seconds.")

def run_in_vm(cmd, quiet=False, log_file=None):
    full_cmd = ["./houdini", "--run_command_in_vm"] + cmd
    if quiet:
        result = subprocess.run(full_cmd, capture_output=True, text=True)
        return result.stdout
    else:
        print(f"Running: {' '.join(full_cmd)}")
        with open(log_file, "a") if log_file else subprocess.DEVNULL as f:
            subprocess.run(full_cmd, stdout=f, stderr=f, text=True)
        return None

def load_config(trick_name):
    config_module = importlib.import_module(f"{trick_name}")
    config = {}
    for var in ["pid_mode", "cap_kill", "cap_sys_ptrace", "privileged_opts", "apparmor_profiles", "user",  "net_bind_service", "cap_drop_all", "runtime"]:
        config[var] = getattr(config_module, var, None)
    return config

def generate_combinations(config):
    fields = [
        config.get("pid_mode") or [None],
        config.get("cap_kill") or [False],
        config.get("cap_sys_ptrace") or [False],
        config.get("privileged_opts") or [False],
        config.get("apparmor_profiles") or [None],
        config.get("user") or [None],
        config.get("net_bind_service") or [None],
        config.get("cap_drop_all") or [None],
        config.get("runtime") or [None]
    ]
    return list(itertools.product(*fields))[:MAX_TESTS]

def build_docker_image():
    print("Building Docker image...")
    build_output = run_in_vm(["docker", "build", "-q", f"/houdini/tricks/{TRICK}"], quiet=True)
    print("Raw build output:", build_output)
    matches = re.findall(r"sha256:([a-f0-9]{64})", build_output)
    if matches:
        image_id = matches[-1][:12]
        print(f"Image ID: {image_id}")
        return image_id
    else:
        raise RuntimeError("Failed to extract image ID from build output.")

def run_tests(image_id, combinations, version):
    log_path = os.path.join(LOG_DIR, f"{TRICK}_{version}.log")
    for idx, (pid_mode, kill, ptrace, privileged, apparmor, user, net_bind_service, cap_drop_all, runtime) in enumerate(combinations):
        with open(log_path, "a") as f:
            f.write(f"\n=== Test #{idx + 1} ===\n")

        cmd = ["docker", "run", "-i"]

        if pid_mode:
            cmd.append(str(pid_mode))

        if privileged:
            cmd.append("--privileged")

        if isinstance(kill, str):
            cmd += ["--cap-add", "CAP_KILL"]

        if ptrace:
            cmd += ["--cap-add", "CAP_SYS_PTRACE"]

        if apparmor:
            cmd += ["--security-opt", str(apparmor)]

        if user:
            cmd += ["--user", str(user)]

        if isinstance(net_bind_service, str):
            cmd += ["--cap-add", "NET_BIND_SERVICE"]

        if cap_drop_all:
            cmd += ["--cap-drop", "ALL"]

        if isinstance(runtime, str):
            cmd += ["--runtime", str(runtime)]

        cmd.append(str(image_id))

        with open(log_path, "a") as f:
            f.write("Running container with flags: " + " ".join(map(str, cmd)) + "\n")

        run_in_vm(cmd, quiet=False, log_file=log_path)


def kill_old_qemu_vms():
    try:
        subprocess.run(["pkill", "-f", "qemu-system-x86_64"], check=False, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"⚠️ Failed to kill QEMU VMs: {e}")



def main():
    ensure_log_dir()
    log_path = os.path.join(LOG_DIR, f"{TRICK}_{DOCKER_ENGINE_VERSION}.log")

    if os.path.exists(log_path):
        print(f"⏭️  Skipping Trick. {log_path} — log already exists.")
        return

    print(f"🚀 Running test for Docker {DOCKER_ENGINE_VERSION}...")
    update_docker_engine_version(DOCKER_ENGINE_VERSION)
    start = time.time()
    
    # mkfs()
    start_vm()
    wait_for_port()
    time.sleep(20)
    config = load_config(TRICK)
    combinations = generate_combinations(config)
    image_id = build_docker_image()
    run_tests(image_id, combinations, DOCKER_ENGINE_VERSION)
    kill_old_qemu_vms()

if __name__ == "__main__":
    main()
