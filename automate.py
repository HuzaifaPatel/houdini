import subprocess
import itertools
import re
import sys
import socket
import time
import importlib
sys.path.append('constants')
sys.path.append('trick_configs')
from houdini_config import *

# === CONFIGURATION ===
MAX_TESTS = 32  # Set to total number of combinations or any N <= 32

def mkfs():
    subprocess.run(["./houdini", "--mkfs"], check=True)

def start_vm():
    subprocess.run(["./houdini", "--start_vm"], check=True)

def wait_for_port(host="127.0.0.1", port=49153, timeout=30):
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


def run_in_vm(cmd, quiet=False):
    full_cmd = ["./houdini", "--run_command_in_vm"] + cmd
    if quiet:
        result = subprocess.run(full_cmd, capture_output=True, text=True)
        return result.stdout
    else:
        print(f"Running: {' '.join(full_cmd)}")
        process = subprocess.Popen(full_cmd)
        process.communicate()
        return None

def load_config(trick_name):
    config_module = importlib.import_module(f"{trick_name}")
    config = {}

    for var in ["pid_modes", "cap_kill", "cap_sys_ptrace", "privileged_opts", "apparmor_profiles", "user"]:
        if hasattr(config_module, var):
            config[var] = getattr(config_module, var)
        else:
            config[var] = None  # fallback

    return config

def generate_combinations(config):
    fields = [
        config.get("pid_modes") or [None],
        config.get("cap_kill") or [False],
        config.get("cap_sys_ptrace") or [False],
        config.get("privileged_opts") or [False],
        config.get("apparmor_profiles") or [None],
        config.get("user") or [None]
    ]
    combinations = list(itertools.product(*fields))
    return combinations[:MAX_TESTS]


def build_docker_image():
    print("Building Docker image...")
    build_output = run_in_vm(["docker", "build", "-q", f"/houdini/tricks/{TRICK}"], quiet=True)
    matches = re.findall(r"sha256:([a-f0-9]{64})", build_output)
    print("Raw build output:", build_output)
    if matches:
        image_id = matches[-1][:12]  # Docker-style short ID
        print(f"Image ID: {image_id}")
        return image_id
    else:
        raise RuntimeError("Failed to extract image ID from build output.")

def run_tests(image_id, combinations):
    for idx, (pid_mode, kill, ptrace, privileged, apparmor, user) in enumerate(combinations):
        print(f"\n=== Test #{idx + 1} ===")
        cmd = ["docker", "run", "-i"]

        if pid_mode:
            cmd.append(pid_mode)
        if privileged:
            cmd.append("--privileged")
        if kill:
            cmd += ["--cap-add", "CAP_KILL"]
        if ptrace:
            cmd += ["--cap-add", "CAP_SYS_PTRACE"]
        if apparmor:
            cmd += ["--security-opt", apparmor]
        if user:
            cmd += ["--user", user]

        cmd.append(image_id)
        print("Running container with flags:", " ".join(cmd))
        run_in_vm(cmd, quiet=False)

def main():
    mkfs()
    start_vm()
    wait_for_port()

    config = load_config(TRICK)
    combinations = generate_combinations(config)
    image_id = build_docker_image()
    run_tests(image_id, combinations)

if __name__ == "__main__":
    main()
