from flask import Flask, jsonify, request, make_response
import server_utils
import subprocess
import hashlib
from server_utils import *
app = Flask(__name__)

@app.route('/server-status', methods=['GET'])
def server_status():
    if is_service_running('houdini-server'):
        response_data = str(True)
        response = make_response(response_data, 200)
    else:
        response_data = str(False)
        response = make_response(response_data, 503)

    response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

    return response

@app.route('/apparmor-status', methods=['GET'])
def apparmor_status():
    if is_service_running('apparmor'):
        response_data = str(True)
        response = make_response(response_data, 200)
    else:
        response_data = str(False)
        response = make_response(response_data, 404)
    
    response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

@app.route('/selinux-status', methods=['GET'])
def selinux_status():
    if is_service_running('selinux'):
        response_data = str(True)
        response = make_response(response_data, 200)
    else:
        response_data = str(False)
        response = make_response(response_data, 404)

    response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace with the VM's IP address