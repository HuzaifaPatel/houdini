def run_trick(trick):
    import requests
    import json
    from houdini_config import VM_URL, get_value
    metadata = {
        'PRIV_MODE': get_value('PRIV_MODE'),
        'APPARMOR': get_value('APPARMOR')
    }

    response = requests.get(f'{VM_URL}/run-trick/{trick}', params=metadata)
    data = response.text

    print(data)

def for_host_debug():
    import requests
    import json
    PORT = 49153
    VM_URL = f'http://127.0.0.1:{PORT}'
    trick = "host_network_namespace"

    response = requests.get(f'{VM_URL}/run-trick/{trick}')
    data = response.text

    print(data)

for_host_debug()