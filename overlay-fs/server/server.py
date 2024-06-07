from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json  # Assuming the data is sent as JSON
    # Process the data...
    return 'Data received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace with the VM's IP address
