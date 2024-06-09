from flask import Flask, jsonify, request
import utils.py
import subprocess

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    data = request.args  # Assuming the data is sent as JSON

    return jsonify(status=is_service_running())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace with the VM's IP address