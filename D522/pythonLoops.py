# Python loops are control flow structures used to repeatedly execute a block of code

# A for loop is used to iterate over a sequence (list, tuple, dictionary, string, or range)
# A while loop is used to repeatedly execute a block of code as long as a certain condition
# is true.

# Example:

subnet = '192.168.1.'
ip_addresses = [subnet + str(i) for i in range(1, 256)]

for ip in ip_addresses:
    print(ip)

# Constructing while Loops

# Example
subnet = '192.168.1.'
ip_addresses = []
i = 1

while i < 256:
    ip_addresses.append(subnet + str(i))
    i += 1

for ip in ip_addresses:
    print(ip)

# Incrementing in a while Loop

# The increment in a while loop is a step that increases a counter variable. Its necessary to
# prevent the loop from running indefinitely, ensuring that the loop condition eventually 
# becomes False, thus terminating the loop.

# Example

number = 0

while number < 5:
    print(number)
    number += 1

#########################################################################

# The break statement
# The break statement in Python is used to exit a loop prematurely. Its used when there
# is a need to stop the loop even if the loops condition has not become False

subnet = '192.168.1.'

ip_addresses = []

i = 1

while True:
    if i > 255:
        break
    ip_addresses.append(subnet + str(i))
    i += 1

for ip in ip_addresses:
    print(ip)

#########################################################################

# The continue statement
# The continue statement is Python is used in loops to skip the rest of the current iteration
# and move directly to the next one.

# Example:

subnet = '192.168.1.'

ip_addresses = []

i = 0

while i < 256:
    i += 1
    if i == 100: # this will skip the 192.168.1.100 ip
        continue
    ip_addresses.append(subnet, str(i))

for ip in ip_addresses:
    print(ip)

#########################################################################

# The else statement
# The else statement in a Python while loop specifies a block of code to be executed when the
# loop condition becomes False. The else block executes after the loop finishes, but not if the 
# loop exited prematurely with a break statement.

# Example:

subnet = '192.168.1.'

ip_addresses = []

i = 0

while i < 256:
    i += 1
    ip_addresses.append(subnet + str(i))
else:
    print('All IP addresses have been generated.')

for ip in ip_addresses:
    print(ip)
