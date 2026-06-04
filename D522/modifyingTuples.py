# Define a tuple

network_device = ('192.168.1.1', 'cisco', 'admin', 'password')

# Access the IP Address

ip_address = network_device[0]

# Access the device type

device_type = network_device[1]

print(f'IP address: {ip_address}, Device type: {device_type}')

#########################################################################

# Define a tuple

network_device = ('192.168.1.1', 'cisco', 'admin', 'password', 'port 22', 'ssh')

# Access a range of items in the tuple

credentials = network_device[2:5]

print(f'Credentials: {credentials}')

#########################################################################

# Define a tuple

network_device = ('192.168.1.1', 'cisco', 'admin', 'password', 'port 22', 'ssh')

# Access a range of items in the tuple using negative indexes

connection_info = network_device[-3:]

print(f'Connection Info: {connection_info}')

########################################################################

# Checking if an item exists in a tuple

# Define a tuple

network_device = ('192.168.1.1', 'cisco', 'admin', 'password')

# Check if 'cisco' is in the tuple

device_exists = 'cisco' in network_device

print(f'Device exists: {device_exists}')
