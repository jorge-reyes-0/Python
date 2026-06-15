# D522 - Dictionaries
# Covers: creation, access, nested dicts, dict() constructor,
#         updating, adding, removing, and clearing items.

# ---------------------------------------------------------------------------
# Basic dictionary — maps device names to IP addresses
network_devices = {
    'Router1':   '192.168.1.1',
    'Switch1':   '10.0.0.1',
    'Firewall1': '172.16.0.1',   # fixed: was 172.160.0.1
    'Server1':   '192.168.2.1',
}

router_ip = network_devices['Router1']
network_devices['Switch2'] = '10.0.0.2'   # add new entry

print(network_devices)
print(router_ip)

# ---------------------------------------------------------------------------
# Nested dictionaries — each device holds its own attribute dict
device_info = {
    'Router1':   {'ip': '192.168.1.1', 'vendor': 'Cisco',    'os': 'IOS'},
    'Switch1':   {'ip': '10.0.0.1',    'vendor': 'Cisco',    'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1',  'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}
print(device_info)

# ---------------------------------------------------------------------------
# dict() constructor — convert a list of (key, value) tuples
device_list = [('Router5', '192.168.3.1'), ('Switch1', '10.3.3.3'), ('Firewall6', '172.1.1.1')]
network_devices = dict(device_list)
print(network_devices)

# ---------------------------------------------------------------------------
# Accessing values by key
device_info = {'ip_address': '192.168.1.1', 'hostname': 'switch1', 'model': 'Cisco 3750'}
print(f"IP: {device_info['ip_address']}, Host: {device_info['hostname']}, Model: {device_info['model']}")

# ---------------------------------------------------------------------------
# Modifying values
network_devices = {
    'Router1':   '192.168.1.1',
    'Switch1':   '10.0.0.1',
    'Firewall1': '172.16.0.1',
    'Server1':   '192.168.2.1',
}
network_devices['Router1'] = '192.168.1.100'
print(network_devices)

# Modifying a value inside a nested dict
device_info = {
    'Router1':   {'ip': '192.168.1.1', 'vendor': 'Cisco',    'os': 'IOS'},
    'Switch1':   {'ip': '10.0.0.1',    'vendor': 'Cisco',    'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1',  'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}
device_info['Router1']['ip'] = '192.168.1.100'
print(device_info)

# ---------------------------------------------------------------------------
# Removing items — del or pop()
network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
del network_devices['Switch']
# value = network_devices.pop('Switch')  # alternative — also returns the removed value
print(network_devices)

# ---------------------------------------------------------------------------
# update() — merge another dict in, overwriting matching keys
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key2': 'new_value2', 'key3': 'value3'}
dict1.update(dict2)
print(dict1)

device_info = {'ip_address': '192.168.1.1', 'hostname': 'switch1', 'model': 'Cisco 3750'}
device_info.update({'model': 'Cisco 3850', 'os_version': '15.2'})
print(device_info)

# ---------------------------------------------------------------------------
# Adding an item
network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
network_devices['Firewall'] = '192.168.1.4'
print(network_devices)

# ---------------------------------------------------------------------------
# Clearing a dictionary
network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
network_devices.clear()
print(network_devices)   # {}
