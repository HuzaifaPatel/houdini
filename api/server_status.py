import requests
import json
from houdini_config import VM_URL

def server_status():
    try:
        response = requests.get(f'{VM_URL}/server-status')

        if response.status_code == 200:
            print("The server is running.")
        elif response.status_code == 503:
            print("The server is not running.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")