import requests
import json
from houdini_config import VM_URL

def run_command_in_vm(command):
    try:
        response = requests.get(f'{VM_URL}/run-command-in-vm', params={'cmd': command})
        if response.status_code == 200:
            data = response.json()
            print("Command output:")
            print(data['output'])
        else:
            print(f"Failed to run command. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")