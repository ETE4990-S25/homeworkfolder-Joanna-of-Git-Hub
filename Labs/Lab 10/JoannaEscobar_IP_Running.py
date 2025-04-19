import docker

#My Code
server = docker.from_env()

#check the IP address
def check_ip_status(name):
    
    specific_container = server.containers.get(name)
    # I couldn't figure out another way to show the IP address, so I used
    # Mr. Power's code
    networks = specific_container.attrs['NetworkSettings']['Networks']
    
    for net_name, net_data in networks.items():
        print(f"{name} in network '{net_name}' has IP: {net_data['IPAddress']}")

# Mr. Powers's Code, just condensed
# client = docker.from_env()

# def list_running_containers():
#     containers = client.containers.list(all=True)# list all containers
#     #containers = client.containers.list() #list only running containers
#     for container in containers:
#         print(f"{container.name} - {container.status}")


# def show_container_ip(container_name):
#     container = client.containers.get(container_name)
#     networks = container.attrs['NetworkSettings']['Networks']
    
#     for net_name, net_data in networks.items():
#         print(f"{container_name} in network '{net_name}' has IP: {net_data['IPAddress']}")