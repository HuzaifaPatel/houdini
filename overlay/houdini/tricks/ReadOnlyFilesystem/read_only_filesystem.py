import os
import subprocess

def is_read_only(mount_point):
    """
    Check if the filesystem at the given mount point is read-only.

    Args:
        mount_point (str): The path to the mount point.

    Returns:
        bool: True if the filesystem is read-only, False otherwise.
    """
    try:
        # Use the `mount` command to check filesystem options
        output = subprocess.check_output(['mount'], text=True)
        for line in output.splitlines():
            if mount_point in line and 'ro,' in line:
                return True
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking filesystem mount options: {e}")
        return False

def test_write_permission(test_file_path):
    """
    Attempt to write to a test file to check write permissions.

    Args:
        test_file_path (str): Path to the test file.

    Returns:
        bool: True if write operation is successful, False otherwise.
    """
    try:
        with open(test_file_path, 'w') as test_file:
            test_file.write("Testing write permissions.")
        # Cleanup
        os.remove(test_file_path)
        return True
    except IOError:
        return False

def main():
    mount_point = '/'  # Change this to the actual mount point
    test_file_path = os.path.join(mount_point, 'test_write_permission.tmp')

    # Check if the filesystem is read-only
    if is_read_only(mount_point):
        print(f"Filesystem at {mount_point} is mounted as read-only.\r")
    else:
        print(f"Filesystem at {mount_point} is not read-only.")

    # Test write permissions
    if test_write_permission(test_file_path):
        print(f"Write permissions are available on {mount_point}.")
    else:
        print(f"Filesystem at {mount_point} is confirmed as read-only.")

if __name__ == "__main__":
    main()
