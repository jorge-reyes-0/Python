# Example of a simple network automation using if / else

device_status = 'online'

# Check if the device is online

if device_status == 'online':
    print('Device is online. Proceed with configuration')
else:
    print('Device is offline. Unable to perform configuration')

############################################################################

# Branches
# A branch is a set of statements that are only executed when certain conditions are met.
# In flowcharts, a decision creates two branches. If the decision is true, then the first
# branch executes. Otherwise, the second branch executes.

############################################################################

# Pseudocode
# Is a high-level description of an algorithm or a program written in a way that is easy for
# humans to understand. 

# Pseudocode for a if/else statement

if condition is true:
    # Code to be executed if the condition is true
    perform action A
else:
    # Code to be executed if the condition is false
    perform action B

############################################################################

# Conditional Expressions
# Shorthand if/else

# Syntax of a shorthand if/else

# Assume there is a function is_device_up(device_ip) that returns true if the device
# is up and false if its down

device_ip = '192.168.1.1' # IP address of the network device

status = 'up' if is_device_up(device_ip) else 'down'
print(f'Device {device_ip} is {status}')

