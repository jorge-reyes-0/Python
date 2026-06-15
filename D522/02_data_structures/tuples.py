# D522 - Tuples
# Covers: creation, indexing, slicing, unpacking, length,
#         tuple() constructor, and modifying via list conversion.

# ---------------------------------------------------------------------------
# Basic tuple access
network_device = ('192.168.1.1', 'cisco', 'admin', 'password')

ip_address  = network_device[0]
device_type = network_device[1]
print(f'IP address: {ip_address}, Device type: {device_type}')

# ---------------------------------------------------------------------------
# Slicing a tuple
network_device = ('192.168.1.1', 'cisco', 'admin', 'password', 'port 22', 'ssh')

credentials   = network_device[2:5]    # items at index 2, 3, 4
connection_info = network_device[-3:]  # last 3 items
print(f'Credentials: {credentials}')
print(f'Connection Info: {connection_info}')

# ---------------------------------------------------------------------------
# Membership test
network_device = ('192.168.1.1', 'cisco', 'admin', 'password')
device_exists = 'cisco' in network_device
print(f'Device exists: {device_exists}')

# ---------------------------------------------------------------------------
# Unpacking a tuple — assign each position to a named variable
network_device = ("192.168.1.1", "cisco", "admin", "password")
ip_address, device_type, username, password = network_device
print(f'Connecting to device {device_type} at {ip_address} using username {username}')

# ---------------------------------------------------------------------------
# Tuple length
network_devices = ('Router1', 'Switch1', 'Firewall1', 'Server1')
num_devices = len(network_devices)
print(f'The number of network devices is: {num_devices}')

# ---------------------------------------------------------------------------
# Single-item tuple — the trailing comma is required
username_tuple = ('admin',)
(username,) = username_tuple
print(f'Username: {username}')

# ---------------------------------------------------------------------------
# tuple() constructor — convert a list to a tuple
network_device_info = ['192.168.1.1', 'cisco', 'admin', 'password']  # fixed: was '192.1681.1.'
network_device = tuple(network_device_info)
print(f'Network device: {network_device}')

# ---------------------------------------------------------------------------
# Modifying a tuple — tuples are immutable, so convert to list, edit, convert back
network_device = ('192.168.1.1', 'cisco', 'admin', 'password')
device_list = list(network_device)
device_list[0] = '192.168.2.2'
network_device = tuple(device_list)
print(f'Network device: {network_device}')

# ---------------------------------------------------------------------------
# "Adding" items — concatenate with another tuple
network_device  = ('192.168.1.1', 'cisco', 'admin', 'password')
additional_info = ('port 22', 'ssh')
network_device  = network_device + additional_info
print(f'Network device: {network_device}')

# ---------------------------------------------------------------------------
# "Removing" an item — convert to list, remove, convert back
device_info = ('192.168.1.1', 'switch1', 'Cisco 3750')
device_list = list(device_info)
device_list.remove('Cisco 3750')
device_list.append('Cisco 3850')
device_info = tuple(device_list)
print(f'Device info: {device_info}')
