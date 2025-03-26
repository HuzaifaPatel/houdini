import os

def test_write_permission(test_file_path):
    """
    Attempt to create a test file to check write permissions.

    Args:
        test_file_path (str): Path to the test file.

    Returns:
        bool: True if file creation is successful, False otherwise.
    """
    try:
        # Attempt to create and write to the test file
        with open(test_file_path, 'w') as test_file:
            test_file.write("Testing write permissions.")
        # Cleanup: Remove the test file if successfully created
        os.remove(test_file_path)
        return True
    except IOError as e:
        print(f"IOError: {e}")
        return False

def main():
    mount_point = '/'  # Change this to the desired mount point
    test_file_path = os.path.join(mount_point, 'test_write_permission.tmp')

    # Test write permissions by trying to create a file
    if test_write_permission(test_file_path):
        print(f"Write permissions are available on {mount_point}.")
    else:
        print(f"Filesystem at {mount_point} appears to be read-only or permission is denied.")

if __name__ == "__main__":
    main()
