from flask import Flask, jsonify, request, make_response, Response
import subprocess
import hashlib
from server_utils import *
import io
import sys
import os
import contextlib
app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

# houdini server status
@app.route('/server-status', methods=['GET'])
def server_status():
    if is_service_running('/usr/bin/python3 /houdini/server.py'):
        response_data = str(True)
        response = make_response(response_data, 200)
    else:
        response_data = str(False)
        response = make_response(response_data, 503)

    # response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

    return response

#kernel, docker, runc versions
@app.route('/version-status', methods=['GET'])
def version_status():
    versions = get_version()
    response_data = jsonify(versions)    

    response = make_response(response_data, 200)
    # response.headers['X-Checksum'] = hashlib.sha512(response_data.encode()).hexdigest()

    return response

@app.route('/run-trick/<trick_folder>/<trick>', methods=['GET'])
def run_trick(trick_folder, trick):

    # version_status()
    # TRICK_PATH = f'tricks/{trick_folder}/{trick}' # for host

    TRICK_PATH = f'/houdini/tricks/{trick_folder}/{trick}'
    # Check if the file exists
    if not os.path.exists(TRICK_PATH):
        return jsonify({'error': f'Trick {trick} not found. PATH = {TRICK_PATH}'}), 404

    # Assuming your YAML configuration is stored in a file named 'config.yaml'
    with open(TRICK_PATH, 'r') as file:
        trick_data = yaml.safe_load(file)

    output = io.StringIO()

    with contextlib.redirect_stdout(output):
        results = parse_trick_and_run(trick_data, request.args)

    return Response(output.getvalue())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=49153, debug=True)  # Replace with the VM's IP address