import subprocess

def is_service_running(service_name='houdini'):
    try:
        subprocess.run(['systemctl', 'is-active', service_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False