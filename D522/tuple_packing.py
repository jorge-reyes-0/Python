# Define a tuple for a network device

network_device = ("192.168.1.1", "cisco", "admin", "password")

# Unpack the tuple

ip_address, device_type, username, password = network_device

# Use the unpacked values

print(f'Connecting to device {device_type} at {ip_address} using username {username}')
