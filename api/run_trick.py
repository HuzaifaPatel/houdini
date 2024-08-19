import requests
import json
from houdini_config import VM_URL, get_value

def run_trick(trick):
    metadata = {
        'PRIV_MODE': get_value('PRIV_MODE'),
        'APPARMOR': get_value('APPARMOR')
    }

    response = requests.get(f'{VM_URL}/run-trick/{trick}', params=metadata)
    data = response.text

    print(data)