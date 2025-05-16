import os
import ctypes
import time

PTRACE_ATTACH = 16
libc = ctypes.CDLL("libc.so.6")

def ptrace_test(target_pid):
    ret = libc.ptrace(PTRACE_ATTACH, target_pid, None, None)
    if ret == 0:
        print(f"✅ ptrace succeeded on PID {target_pid}")
        os.waitpid(target_pid, 0)
    else:
        errno = ctypes.get_errno()
        print(f"❌ ptrace failed on PID {target_pid}, errno: {errno}")

if __name__ == "__main__":
    pid = os.fork()
    
    if pid == 0:
        # Child process: Simulate a long-running target process
        print(f"Target process started with PID {os.getpid()}")
        time.sleep(1000)  # Keep the child alive for tracing
    else:
        # Parent process: Give the child a moment to start
        time.sleep(1)
        ptrace_test(pid)
