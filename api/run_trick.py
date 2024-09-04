def run_trick(trick):
    import requests
    import json
    from houdini_config import VM_URL, get_value
    params = {
        'container_name': trick,
        'file': "85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt",
    }

    response = requests.get(f'{VM_URL}/run-trick/{trick}', params=params)
    data = response.text

    print(data)

def for_host_debug():
    import requests
    import json
    PORT = 49153
    VM_URL = f'http://127.0.0.1:{PORT}'
    trick = "read_only_filesystem" # this will be the container name too

    params = {
        'container_name': trick,
        'file': "85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt",
    }

    response = requests.get(f'{VM_URL}/run-trick/{trick}', params=params)
    data = str(response.text)
    
    print(data)


for_host_debug()

# routine is a collection of tricks

# filesystem
# network tests
# ipc tests
# CVE
# memory/cpu