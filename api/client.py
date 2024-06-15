import requests
import json
# import procedure
PORT = 5005
VM_URL = f'http://127.0.0.1:{PORT}'

def check_server_status():
    try:
        response = requests.get(f'{VM_URL}/server-status')

        if response.status_code == 200:
            print("The server is running.")
        elif response.status_code == 503:
            print("The server is not running.")

        # Optionally, you can check the checksum header
        # checksum = response.headers.get('X-Checksum')
        # if checksum:
        #     print(f"Response checksum: {checksum}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def check_versions():
    response = requests.get(f'{VM_URL}/version-status')
    if response.status_code == 200:
        data = json.loads(response.text)
        for key, value in data.items():
            if value.strip():  # Check if the value is not empty after stripping whitespace
                print(f"{key}: {value.strip()}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def run_trick():
    response = requests.get(f'{VM_URL}/run-trick')
    data = response.text

    print(data)


run_trick()