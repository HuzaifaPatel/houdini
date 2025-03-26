def convert_to_camel_case(snake_str):
    # Split the string by underscores
    components = snake_str.split('_')
    
    # Capitalize the first letter of each component and join them together
    camel_case_str = ''.join(x.capitalize() for x in components)
    
    return camel_case_str

def run_trick(trick):
    import requests
    import json
    from houdini_config import VM_URL, get_value
    params = {
        'container_name': trick,
        'file': "85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt",
    }
    # response = requests.get(f'{VM_URL}/run-trick/{convert_to_camel_case(trick)}/{trick}', params=params)
    response = requests.get(f'{VM_URL}/run-trick/{convert_to_camel_case(trick)}/{trick}', params=params)
    data = response.text
    print(data)


def for_host_debug():
    import requests
    import json
    PORT = 49153
    VM_URL = f'http://127.0.0.1:{PORT}'
    trick = "host_mount" # this will be the container name too

    params = {
        'container_name': trick,
        'file': "85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt",
    }

    response = requests.get(f'{VM_URL}/run-trick/{convert_to_camel_case(trick)}/{trick}', params=params)
    data = str(response.text)
    
    print(data)


# for_host_debug()

# routine is a collection of tricks

# filesystem
# network tests
# ipc tests
# CVE
# memory/cpu