# D522 - Lists
# Covers: accessing items, concatenation, copying, list constructor, sorting.

# ---------------------------------------------------------------------------
# Accessing items — list of dicts is a common pattern for network inventories
devices = [
    {"hostname": "router1",   "ip": "192.168.1.1", "type": "router"},
    {"hostname": "switch1",   "ip": "192.168.1.2", "type": "switch"},
    {"hostname": "firewall1", "ip": "192.168.1.3", "type": "firewall"},
]

second_device = devices[1]
hostname    = second_device["hostname"]
ip_address  = second_device["ip"]
device_type = second_device["type"]
print(f"Device: {hostname}, IP: {ip_address}, Type: {device_type}")

# ---------------------------------------------------------------------------
# Concatenating lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# + creates a new list
concatenated = list1 + list2
print(concatenated)

# extend() modifies list1 in place
list1.extend(list2)
print(list1)

# ---------------------------------------------------------------------------
# Copying a list — both methods create a shallow copy
network_devices = ['Switch1', 'Router1', 'Firewall1']
backup_copy1 = network_devices.copy()
backup_copy2 = list(network_devices)
print(backup_copy1)
print(backup_copy2)

# ---------------------------------------------------------------------------
# List constructor — split a CSV string into a list
device_names_string = "router1,switch1,firewall,router2,switch2"
device_names_list = list(device_names_string.split(','))
print(device_names_list)

# ---------------------------------------------------------------------------
# Sorting and reversing
ip_addresses = ["192.168.1.3", "192.168.1.1", "192.168.1.2"]  # fixed: removed trailing dot

ip_addresses.sort()
print(ip_addresses)

ip_addresses.reverse()
print(ip_addresses)
