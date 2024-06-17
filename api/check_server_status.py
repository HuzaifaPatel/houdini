from config import *

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


check_server_status()