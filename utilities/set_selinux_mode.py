from path_manager import get_absolute_path
from houdini_config import get_value
import fileinput

def update_selinux_config():
    try:
        # Use fileinput to read and modify the file in place
        with fileinput.FileInput(get_absolute_path("/overlay/etc/selinux/config"), inplace=True) as file:
            for line in file:
                if line.startswith("SELINUX="):
                    print(f"SELINUX={get_value("SELINUX")}")
                else:
                    print(line, end='')
    except Exception as e:
        print(f"An error occurred: {e}")