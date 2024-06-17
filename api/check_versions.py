from config import *

def check_versions():
    response = requests.get(f'{VM_URL}/version-status')
    if response.status_code == 200:
        data = json.loads(response.text)
        for key, value in data.items():
            if value.strip():  # Check if the value is not empty after stripping whitespace
                print(f"{key}: {value.strip()}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

check_versions()