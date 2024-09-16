# host_ipc.py (Host side)
import mmap
import os

# Path to the shared memory file
shm_file = "/dev/shm/shared_memory"

# Write data to shared memory
def write_to_shared_memory():
    with open(shm_file, "wb") as f:
        # Initialize with 100 bytes
        f.write(b" " * 100)
    
    with open(shm_file, "r+b") as f:
        # Create memory-mapped file
        mm = mmap.mmap(f.fileno(), 100)
        # Write some data
        mm.write(b"Hello from the Host!")
        mm.close()

if __name__ == "__main__":
    if not os.path.exists(shm_file):
        # Create shared memory file
        open(shm_file, 'a').close()
    write_to_shared_memory()
    print(f"Data written to shared memory: {shm_file}")
