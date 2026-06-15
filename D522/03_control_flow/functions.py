# D522 - Functions
# Covers: definition, arguments, keyword args, arbitrary args (*args / **kwargs),
#         default parameters, passing lists, return values, and recursion.

# ---------------------------------------------------------------------------
# Basic function with a positional argument
def add_device(network_devices, device):
    network_devices.add(device)
    return network_devices

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices = add_device(network_devices, 'Load Balancer')
print(network_devices)

# ---------------------------------------------------------------------------
# Arbitrary positional arguments (*args) — accepts any number of values
def function_name(*args):
    for arg in args:
        print(arg)

# ---------------------------------------------------------------------------
# Keyword arguments — caller uses parameter names, order doesn't matter
def configure_device(device_type='Switch', ip_address='192.168.1.1'):
    pass  # function body would go here

# ---------------------------------------------------------------------------
# Arbitrary keyword arguments (**kwargs) — accepts any number of named settings
def configure_device_kwargs(**settings):
    for setting, value in settings.items():
        print(f'Setting {setting} to {value}')

configure_device_kwargs(ip_address='192.168.1.1', subnet_mask='255.255.255.0', gateway='192.168.1.254')

# ---------------------------------------------------------------------------
# Default parameter values — used when the caller omits the argument
def configure_device_default(device, ip_address='192.168.1.1'):
    pass

# ---------------------------------------------------------------------------
# Passing a list as an argument
def configure_devices(device_list):
    for device in device_list:
        print(f'Configuring {device}')

devices = ['Switch', 'Router', 'Firewall']
configure_devices(devices)

# ---------------------------------------------------------------------------
# Return value — functions send results back with the return statement
def count_devices(network_devices):
    return len(network_devices)

# ---------------------------------------------------------------------------
# Recursion — a function that calls itself
# This walks through a list of servers and returns the first one that is online.
# ping() is assumed to be defined elsewhere and returns True/False.

def find_online_server(servers):
    if len(servers) == 0:
        return None
    elif ping(servers[0]):   # ping() would need to be imported/defined
        return servers[0]
    else:
        return find_online_server(servers[1:])
