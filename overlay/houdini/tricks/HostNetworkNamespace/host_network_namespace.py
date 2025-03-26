import requests
import os
import socket

def server_running(host='localhost', port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)  # Set a timeout for the connection attempt
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False


def download_file(url='http://localhost:8000/houdini/tricks/HostNetworkNamespace/85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt', local_filename="85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt"):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Open a local file with the same name as the URL's filename
        with open(local_filename, 'wb') as file:
            # Write the content to the file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File {local_filename} downloaded to container", end="")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    except FileNotFoundError:
        print(f"File {local_filename} could not be created or opened.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if server_running():
        print("Server is Running")
        download_file()
    else:
        print("NOT")