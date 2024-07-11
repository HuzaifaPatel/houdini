import requests
import json
from houdini_config import VM_URL

def run_trick(trick):
    response = requests.get(f'{VM_URL}/run-trick/{trick}')
    data = response.text

    print(data)