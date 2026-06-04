# Define a list with network device information

network_device_info = ['192.1681.1.', 'cisco', 'admin', 'password']

# Use the tuple() constructor to convert the list into a tuple

network_device = tuple(network_device_info)

print(f'Network device: {network_device}')