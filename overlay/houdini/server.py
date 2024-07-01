from flask import Flask, jsonify, request, make_response
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

@app.route('/run-trick', methods=['GET'])
def run_trick():
    # Assuming your YAML configuration is stored in a file named 'config.yaml'
    with open('/houdini/tricks/test.yaml', 'r') as file:
        config_data = yaml.safe_load(file)

    results = parse_trick_and_run(config_data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=49153, debug=True)  # Replace with the VM's IP address