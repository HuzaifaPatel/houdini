import docker

print("Starting Script")
client = docker.APIClient(base_url='unix://var/run/docker.sock')
print("Client Connected")