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

##########################################################################

# Modifying Python sets

# Add items to a set

set1 = {'item1', 'item2', 'item3'}

set1.add('item4')

# To add multiple items to a python set, the update() method is used

set1 = {'item1', 'item2', 'item3'}

set1.update(['item4', 'item5'])

print(set1)

# Example

network_devices = {'Switch', 'Router', 'Firewall'}

network_devices.add('Load Balancer')

print(network_devices)

# Adding sets
# To add items from another set, use the update() method

network_devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Load Balancer', 'Proxy Server'}

network_devices.update(new_devices)

print(network_devices)

# Removing an item from a set
# To remove an item, use the remove() or discard() methods

# The remove() method removes the specified item from a set, but raises an error
# if the item does not exist

# The discard() method also removes but does not raise an error if it doesnt exist

# remove()

set1 = {'item1', 'item2', 'item3'}
set1.remove('item1')

print(set1)

# discard()

set1 = {'item1', 'item2', 'item3'}
set1.discard('item1')

print(set1)

# Emptying a set
# To empty a set, use the clear() method

set1 = {'item1', 'item2', 'item3'}
set1.clear()

# Deleting a set
# Delete a set using the del keyword. Removes the set from memory 
# Results in NameError if you try to use the set

del set1