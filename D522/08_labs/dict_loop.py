def print_device_map(device_map):
    for hostname, ip in device_map.items():
        print(f'Host: {hostname} | IP: {ip}')

# Test your function
device_map = {
    "core-sw-01": "10.1.1.1",
    "dist-sw-02": "10.1.1.2",
    "fw-edge-01": "10.1.1.3",
    "rtr-core-01": "10.1.1.4"
}
print_device_map(device_map)