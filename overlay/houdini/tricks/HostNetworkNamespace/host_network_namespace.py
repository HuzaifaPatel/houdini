import requests
import os

def download_file(url='http://localhost:8000/home/huzi/Desktop/85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt', local_filename="85c8de88d28866bf0868090b3961162bf82392f690d9e4730910f4af7c6ab3ee.txt"):
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

if __name__ == "__main__":
    print("Starting Trick")
    download_file()


