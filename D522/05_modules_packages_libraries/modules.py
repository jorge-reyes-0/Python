# D522 - Python Modules
# A module is a .py file containing functions, classes, or variables that can
# be imported into other scripts to promote code reuse.

# ---------------------------------------------------------------------------
# Importing a module and calling its functions
import mymodule
mymodule.my_function()

# ---------------------------------------------------------------------------
# Renaming a module on import with `as` — useful for long module names
import network as net

ip = '192.168.1.1'
if net.ping_device(ip):
    print(f'Device {ip} is online.')
else:
    print(f'Device {ip} is offline.')

# ---------------------------------------------------------------------------
# Built-in modules — ship with Python, no installation needed
# os and socket are especially useful in network automation.

import socket
import os

hostname   = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f'Hostname: {hostname}')
print(f'IP Address: {ip_address}')

# ---------------------------------------------------------------------------
# dir() lists all attributes/functions in a module
import math
functions = [name for name in dir(math) if callable(getattr(math, name))]
print(functions)

# ---------------------------------------------------------------------------
# Importing only specific items from a module
from network_tools import ping

ip = '192.168.1.1'
if ping(ip):
    print(f'Device {ip} is online')
else:
    print(f'Device {ip} is offline')

# ---------------------------------------------------------------------------
# ipaddress module — enumerate all hosts in a subnet
import ipaddress

network = ipaddress.ip_network('192.168.1.0/24')
for host in network.hosts():
    print(host)

# ---------------------------------------------------------------------------
# Module types overview
#
# Modules      — single .py files with reusable code
# Packages     — directories of modules (must contain __init__.py)
# Libraries    — collections of packages (e.g., Requests, Scapy)
#
# Common network automation modules:
#   netmiko   — SSH to routers and switches
#   NAPALM    — multi-vendor network device API
#   Paramiko  — SSHv2 protocol implementation
#   Ansible   — config management and provisioning
#   Exscript  — Telnet/SSH automation
#   Requests  — HTTP requests
#   Scapy     — packet crafting and capture
