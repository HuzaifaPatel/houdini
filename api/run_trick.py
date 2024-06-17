from config import *

def run_trick():
    response = requests.get(f'{VM_URL}/run-trick')
    data = response.text

    print(data)

run_trick()