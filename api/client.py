import requests
import json
# import procedure

def check_server_status():
    response = requests.get('http://127.0.0.1:5000/server-status')

    if response.status_code == 200:
        print("The server is running.")
    elif response.status_code == 503:
        print("The server is not running.")

    # Optionally, you can check the checksum header
    # checksum = response.headers.get('X-Checksum')
    # if checksum:
    #     print(f"Response checksum: {checksum}")

def check_versions():
    response = requests.get('http://127.0.0.1:5000/version-status')
    if response.status_code == 200:
        data = json.loads(response.text)
        for key, value in data.items():
            if value.strip():  # Check if the value is not empty after stripping whitespace
                print(f"{key}: {value.strip()}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

