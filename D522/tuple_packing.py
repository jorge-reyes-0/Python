# Define a tuple for a network device

network_device = ("192.168.1.1", "cisco", "admin", "password")

# Unpack the tuple

ip_address, device_type, username, password = network_device

# Use the unpacked values

print(f'Connecting to device {device_type} at {ip_address} using username {username}')

###############################################################################################

# Tuple Length 

# Creating the tuple

network_devices = ('Router1', 'Switch1', 'Firewall1', 'Server1')

# Determining the length of the tuple

num_devices = len(network_devices)

print(f'The number of network devices is: {num_devices}')

##############################################################################################

# Tuples with a single item

# Define a tuple with a single item

username = ('admin',)

# Unpack the tuple

(username,) = username

# Use the unpacked value

print(f'Username: {username}')


