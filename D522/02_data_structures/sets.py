# D522 - Sets
# Covers: creation, union, add, update, remove, discard, clear, del.
# Sets store unique, unordered items — no duplicate entries allowed.

# ---------------------------------------------------------------------------
# Union — merge two sets (duplicates are dropped automatically)
network_devices = {'Switch', 'Router', 'Firewall'}
new_devices     = {'Firewall', 'Load Balancer'}
network_devices = network_devices.union(new_devices)
print(network_devices)

# ---------------------------------------------------------------------------
# Creating sets
set_curly  = {'item1', 'item2', 'item3'}           # using curly braces
set_constructor = set(['item1', 'item2', 'item3'])  # using set()

# set() automatically removes duplicates
set_with_dupes = set(['item1', 'item2', 'item3', 'item1'])
set_from_str   = set('hello')   # individual characters become items
print(set_with_dupes, set_from_str)

# ---------------------------------------------------------------------------
# Length of a set
number_of_items = len(set_curly)
print(number_of_items)

# ---------------------------------------------------------------------------
# Accessing items — no indexing; iterate or test membership
for item in set_curly:
    print(item)

if 'item1' in set_curly:
    print('item1 is in the set')

# ---------------------------------------------------------------------------
# add() — insert a single item
network_devices = {'Switch', 'Router', 'Firewall'}
network_devices.add('Load Balancer')
print(network_devices)

# update() — insert multiple items (from a list or another set)
network_devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Load Balancer', 'Proxy Server'}
network_devices.update(new_devices)
print(network_devices)

# ---------------------------------------------------------------------------
# remove() raises KeyError if the item is missing; discard() does not
set1 = {'item1', 'item2', 'item3'}
set1.remove('item1')
print(set1)

set1 = {'item1', 'item2', 'item3'}
set1.discard('item1')
print(set1)

# ---------------------------------------------------------------------------
# clear() empties the set; del removes it from memory entirely
set1 = {'item1', 'item2', 'item3'}
set1.clear()
print(set1)   # set()

set1 = {'item1', 'item2', 'item3'}
del set1
# print(set1)  # would raise NameError
