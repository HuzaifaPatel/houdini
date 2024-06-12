from flask import Flask, jsonify, request, make_response
import server_utils
import subprocess
import hashlib
from server_utils import *
app = Flask(__name__)

# houdini server status
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

#kernel, docker, runc versions
@app.route('/version-status', methods=['GET'])
def version_status():
    versions = get_version()
    response_data = jsonify(versions)    

    response = make_response(response_data, 200)
    # response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

    return response





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace with the VM's IP address