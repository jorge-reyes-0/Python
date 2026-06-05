# Dictionary representing network devices

network_devices = {
    'Router1': '192.168.1.1',
    'Switch1': '10.0.0.1',
    'Firewall1': '172.160.0.1',
    'Server1': '192.168.2.1',
}

# Accessing information about a specific device

router_ip = network_devices['Router1']

# Adding a new device to the dictionary

network_devices['Switch2'] = '10.0.0.2'

print(network_devices)

print(router_ip)

##########################################################

# Creating a dictionary where each device has its own dictionary with keys

device_info = {
    'Router1': {'ip': '192.168.1.1', 'vendor': 'Cisco', 'os': 'IOS'},
    'Switch1': {'ip': '10.0.0.1', 'vendor': 'Cisco', 'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1', 'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}

print(device_info)

##########################################################

# The python dict() constructor

# Creating a dictionary using the constructor for network devices

device_list = [('Router5', '192.168.3.1'), ('Switch1', '10.3.3.3'), ('Firewall6', '172.1.1.1')]

# Using the dictionary constructor to convert the list of tuples into a dictionary

network_devices = dict(device_list)

print(network_devices)

##########################################################

# Accessing dictionary values
# In python, items in dictionary can be accessed using their keys

# Define a dictionary

device_info = {'ip_address': '192.168.1.1', 'hostname': 'switch1', 'model': 'Cisco 3750'}

# Access an item using its key

ip_address = device_info['ip_address']
hostname = device_info['hostname']
model = device_info['model']

print(f'IP: {ip_address}, Host: {hostname}, Model: {model}')