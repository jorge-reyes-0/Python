# Create a module

# Creating a Python module involves writing a Python script with functions, classes, or variables
# and saving it with a .py extension

# That file can be then imported into other Python scripts using the import statement

import mymodule
mymodule.my_function()

# This allows for code reuse across multiple scripts, improving code organization and readability

##############################################################################################

# Renaming a Module

# A module can be renamed when its improted using the as keyword

import network as net

ip = '192.168.1.1'

if net.ping_device(ip):
    print(f'Device {ip} is online.')
else:
    print(f'Device {ip} is offline.')

# In this, network is renamed to net making subsequent calls to the modules functions more concise
# This is useful when dealing with modules that have long names

##############################################################################################

# Built-in Modules

# These are libraries that come pre-installed with Python. They provide functions and classes
# for a variety of tasks without the need for additional installation

# os and socket modules are often used in network automation. The os module provides functions
# for interacting with the operating system, while the socket module is used for network communications

import socket
import os

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f'Hostname: {hostname}')
print(f'IP Address: {ip_address}')

# List Function Names

# To list all function names in a Python module, the dir() function can be used. It returns a
# list of names in the current local scope or a list of attributes of an object. When a module
# is passed as an argument to dir(), it returns a list of the modules attributes including functions

import math

functions = [name for name in dir(math) if callable(getattr(math, name))]

print(functions)

##############################################################################################

# Import from a Module

# Specific parts of a module can be imported using the from .. import .. statement
# Allows for importing only the necessary functions or classes, making code efficient

# Example

from network_tools import ping

ip = '192.168.1.1'

if ping(ip):
    print(f'Device {ip} is online')
else:
    print(f'Device {ip} is offline')

# The ipaddress Module

# Powerful tool for manipulating and analyzing IP addresses and networks. Provides classes for
# handling IPv4 and IPv6 addresses, networks, and interfaces. These classes support validation,
# comparison, sorting, and other operations

# Example:

import ipaddress

# Define the network
network = ipaddress.ip_network('192.168.1.0/24')

# Iterate over all hosts in the network
for host in network.hosts():
    print(host)

##############################################################################################

# The help Module

# Built-in function that can be used to access the built-in documentation for Python modules,
# functions, classes, keywords, etc. Most commonly used in the Python interpreter, and is useful
# for understanding and using different python functionalities