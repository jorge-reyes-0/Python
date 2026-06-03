# List of network devices
devices = [
    {"hostname": "router1", "ip": "192.168.1.1", "type": "router"},
    {"hostname": "switch1", "ip": "192.168.1.2", "type": "switch"},
    {"hostname": "firewall1", "ip": "192.168.1.3", "type": "firewall"},
    # ... (more devices)
]
 
# Retrieve information about the second device (index 1)
second_device = devices[1]
 
# Access specific details using indexing
hostname = second_device["hostname"]
ip_address = second_device["ip"]
device_type = second_device["type"]
 
# Display the information
print(f"Device: {hostname}, IP: {ip_address}, Type: {device_type}")