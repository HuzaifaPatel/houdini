import requests

url = 'http://127.0.0.1:5000/status'  # Replace with the VM's IP address

response = requests.get(url)
print(response.text)  # Print the response from the Flask server
print(response.status_code)
