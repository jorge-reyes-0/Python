# Copying a list to another list

network_devices = ['Switch1', 'Router1', 'Firewall1']
backup_devices = network_devices.copy()

# or

backup_devices = list(network_devices)
print(backup_devices)