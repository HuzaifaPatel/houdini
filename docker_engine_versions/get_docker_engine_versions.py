import requests
import json

# URL for the tags of the moby/moby repository
url = "https://api.github.com/repos/moby/moby/tags"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    tags = response.json()
    
    # Print each tag name
    for tag in tags:
        if "xdocs" not in tag['name'] and "rc" not in tag['name'] and "beta" not in tag['name']:
            print(tag['name'])
            print(tag['commit']['sha'])
else:
    print(f"Failed to fetch tags, status code: {response.status_code}")
