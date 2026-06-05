# Example of a set

network_devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Firewall', 'Load Balancer'}
# Add new devices to the network

network_devices = network_devices.union(new_devices)

print(network_devices)

##########################################################################

# Creating a set

# Using curly braces

set1 = {'item1', 'item2', 'item3'}

# Using the set function

set2 = set(['item1', 'item2', 'item3'])

# Determine the number of items in a set

set1 = {'item1', 'item2', 'item3'}

number_of_items = len(set1)

print(number_of_items)

##########################################################################

# The set() constructor

# Using a list as an argument

set10 = set(['item1', 'item2', 'item3', 'item1'])

# Using a string as an argument

set11 = set('hello')

print(set10, set11)

##########################################################################

# Accessing items in a set
# Items in a set cannot be accessed by index or key, so you must loop through using a for loop
# or ask for a specified value in the set

# Looping through a set

set1 = {'item1', 'item2', 'item3'}

for item in set1:
    print(item)

if 'item1' in set1:
    print('item1 is in the set')