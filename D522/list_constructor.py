# Using list constructor in network automation
device_names_string = "router1,switch1,firewall,router2,switch2"

# Convert comma-separated string into a list

device_names_list = list(device_names_string.split(','))

# Resulting list

print(device_names_list)