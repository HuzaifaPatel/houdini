# RUNC_VERSION = "1.1.11"
# DOCKER_CLI_VERSION = "24.0.0"
# DOCKER_ENGINE_VERSION = "24.0.0"

import os

# Define the relative path
relative_path = '../../../../../'

# Change the current working directory
try:
    os.chdir(relative_path)
    print(f"Successfully changed directory to: {os.getcwd()}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
