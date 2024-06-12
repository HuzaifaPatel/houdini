import subprocess
from config import *

def is_service_running(service_name):
    try:
        subprocess.run(['systemctl', 'is-active', service_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def get_version():
    version_info = {}
    for key, value in versions.items():
        result = subprocess.run(value, check=True, stdout=subprocess.PIPE)
        version_info[key] = result.stdout.decode('utf-8').strip()
    
    return version_info