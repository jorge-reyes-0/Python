# D522 - Conditional Statements (if / else)

# Basic if/else example using device status
device_status = 'online'

if device_status == 'online':
    print('Device is online. Proceed with configuration')
else:
    print('Device is offline. Unable to perform configuration')

# ---------------------------------------------------------------------------
# Branches
# A branch is a set of statements that only execute when a condition is met.
# A True condition runs the first branch; False runs the else branch.

# ---------------------------------------------------------------------------
# Pseudocode example (not runnable Python — just illustrating the concept)
#
#   if condition is true:
#       perform action A
#   else:
#       perform action B

# ---------------------------------------------------------------------------
# Conditional expression (ternary / shorthand if-else)
# Assumes is_device_up(ip) returns True when the device responds to ping.

device_ip = '192.168.1.1'

# status = 'up' if is_device_up(device_ip) else 'down'
# print(f'Device {device_ip} is {status}')
