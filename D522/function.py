def add_devices(network_devices, device):
    network_devices.add(device)
    return network_devices

# Create a set of network devices

network_devices = {'Switch', 'Router', 'Firewall'}

# Call the function to add a new device

network_devices = add_devices(network_devices, 'Load Balancer')

print(network_devices)