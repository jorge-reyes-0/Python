# Creating a dictionary

network_devices = {
    'Router1': '192.168.1.1',
    'Switch1': '10.0.0.1',
    'Firewall1': '172.160.0.1',
    'Server1': '192.168.2.1',
}

# Changing the value of a specific key

network_devices['Router1'] = '192.168.1.100'

print(network_devices)

# Another example

device_info = {
    'Router1': {'ip': '192.168.1.1', 'vendor': 'Cisco', 'os': 'IOS'},
    'Switch1': {'ip': '10.0.0.1', 'vendor': 'Cisco', 'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1', 'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}

# Changing the IP address of a specific device

device_info['Router1']['ip'] = '192.168.1.100'

print(device_info)

###################################################################################

# Removing an item from a dictionary 
# The del keyword or the pop() method can be used

dictionary = {'key1': 'value1', 'key2': 'value2'}

del dictionary['key1']

# or

# value = dictionary.pop('key1')

# Example

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}

del network_devices['Switch']

print(network_devices)

###################################################################################

# Updating a Python Dictionary

# The update() method is used to update a dictionary with the key/value pairs from another
# dictionary, or from an iterable of key/value pairs

# Define two dictionaries

dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key2': 'new_value2', 'key3': 'value3'}

# Update dict1 with dict2

dict1.update(dict2)

print(dict1)

# Example

device_info = {'ip_address': '192.168.1.1', 'hostname': 'switch1', 'model': 'Cisco 3750'}

updated_info = {'model': 'Cisco 3850', 'os_version': '15.2'}

device_info.update(updated_info)

print(device_info)

###################################################################################

# Adding dictionary items
# To add an item to a Python dictionary, assign a value to a new key in the dictionary

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}

network_devices['Firewall'] = '192.168.1.4'

print(network_devices)

###################################################################################

# Clearing a dictionary
# To clear a dictionary, use the clear() method

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
network_devices.clear()

print(network_devices)