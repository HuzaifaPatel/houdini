# container_ipc.py (Container side)
import mmap

# Path to the shared memory file
shm_file = "/dev/shm/shared_memory"

# Read data from shared memory
def read_from_shared_memory():
    with open(shm_file, "r+b") as f:
        # Create memory-mapped file
        mm = mmap.mmap(f.fileno(), 100)
        # Read and print the data
        data = mm.read(100).strip()
        print(f"Data read from shared memory: {data.decode()}")
        mm.close()

if __name__ == "__main__":
    read_from_shared_memory()
