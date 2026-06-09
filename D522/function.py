def add_devices(network_devices, device):
    network_devices.add(device)
    return network_devices

# Create a set of network devices

network_devices = {'Switch', 'Router', 'Firewall'}

# Call the function to add a new device

network_devices = add_devices(network_devices, 'Load Balancer')

print(network_devices)

###############################################################################

# Arguments
# Are values that are passed to a function when it is called. Each argument is treated
# as a variable inside the function. They are used to provide inputs to a function
# so it can perform a task based on those inputs

# Example of a function with arguments

def add_device(network_devices, device):
    network_devices.add(device)
    return network_devices

###############################################################################

# Parameter versus Arguments

# Parameters are variables in a functions definitions. Arguments are actual values passed to a
# function.
# Parameters initialize with arguments. Both terms are often used interchangeably in discussions
# about functions. Both are often used interchangeably

# Arbitrary Arguments

# Allows a function to accept any number of arguments. Useful when the exact number of arguments
# is not known in advance. These are defined by prefixng the argument with an asterisk in 
# the function definition

# Example

def function_name(*args):
    for arg in args:
        print(arg)

# In this case 'args' is a tuple of all the arguments passed to the function. The function
# prints each argument.

###############################################################################

# Keyword Arguments
# These are arguments that are identified by the parameter name in a function call
# The caller identifies the arguments by the parameter name, which allows for the arguments
# to be passed in any order and makes the function call more clear

# Example:

def function_name(keyword1=value1, keyword2=value2):
    # function body
    pass

# Another example:

def configure_device(device_type='Switch', ip_address='192.168.1.1'):
    # function body
    pass

# Arbitrary Keyword Arguments
# These allow a function to accept any number of keyword arguments. Useful when the exact number
# of keyword arguments are not known in advance. They are defined by prefixing the argument name with
# double asterisks in the funciton definition

# Example

def configure_device(**settings):
    for setting, value in settings.items():
        print(f'Setting {setting} to {value}')

configure_device(ip_address='192.168.1.1', subnet_mask='255.255.255.0', gateway='192.168.1.254')

###############################################################################

# Default Parameter Values
# Is a value that is assigned to a function parameter when the function is defined

# Example

def configure_device(device, ip_address='192.168.1.1'):
    pass

###############################################################################

# Passing a list as an argument
# A list can be passed as an argument to a Python funciton just like any other data type.
# The function can then perform operations on the list.

# Example:

def configure_devices(device_list):
    for device in device_list:
        print(f'Configuring {device}')

devices = ['Switch', 'Router', 'Firewall']
configure_devices(devices)

###############################################################################

# Returning a Value
# A python function returns a value using the return statement, the value that follows the return keyword
# is the result that the function sends back when it is called. If no value is specified, the
# the function will return None

def count_devices(network_devices):
    return len(network_devices)

###############################################################################

# Function Recursion
# Is a process in which a function calls itself as a subroutine. This allows the function to be
# repeated several times, as it can call itself during its execution.

# Recursion can be direct or indirect
# Direct recursion occurs if a function calls itself; an indirect recursion involves the function
# calling another function, which eventually results in the original function being called

# Example:

def find_online_server(servers):
    if len(servers) == 0:
        return None
    elif ping(servers[0]):
        return servers[0]
    else:
        return find_online_server(servers[1:])
    