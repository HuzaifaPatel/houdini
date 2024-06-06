import requests

data = {'key': 'value'}  # Your data to be sent
url = 'http://127.0.0.1:5000/receive'  # Replace with the VM's IP address

response = requests.post(url, json=data)
print(response.text)  # Print the response from the Flask server
