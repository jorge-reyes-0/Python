# Define a tuple for a network device
network_device = ('192.168.1.1', 'cisco', 'admin', 'password')

# Convert the tuple into a list

network_device_list = list(network_device)

# Change whatever it is that you want changed

network_device_list[0] = '192.168.2.2'

# Convert the list back into a tuple

network_device = tuple(network_device_list)

print(f'Network device: {network_device}')

###############################################################################

# Adding items to a tuple can be done by concatenating the tuple with another tuple 

# Define a tuple 

network_device = ('192.168.1.1', 'cisco', 'admin', 'password')

# Define a new tuple with additional information

additional_info = ('port 22', 'ssh')

# Concatenate the tuples

network_device = network_device + additional_info

print(f'Network device: {network_device}')

###############################################################################

# Removing items from a tuple

# Original tuple with IP address, hostname, and model

device_info = ('192.168.1.1', 'switch1', 'Cisco 3750')

# Convert tuple to a list

device_list = list(device_info)

# Remove whatever it is you want

device_list.remove('Cisco 3750')

# Add the new model to the list

device_list.append('Cisco 3850')

# Convert the list back to a tuple

device_info = tuple(device_list)

print(f'Device info: {device_info}')



