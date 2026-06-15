# D522 - Loops
# Covers: for loops, while loops, break, continue, and while/else.

# ---------------------------------------------------------------------------
# for loop — generate a /24 IP range using a list comprehension
subnet = '192.168.1.'
ip_addresses = [subnet + str(i) for i in range(1, 256)]

for ip in ip_addresses:
    print(ip)

# ---------------------------------------------------------------------------
# while loop — same result, built iteratively
subnet = '192.168.1.'
ip_addresses = []
i = 1

while i < 256:
    ip_addresses.append(subnet + str(i))
    i += 1

for ip in ip_addresses:
    print(ip)

# ---------------------------------------------------------------------------
# Incrementing a counter — simple while example
number = 0
while number < 5:
    print(number)
    number += 1

# ---------------------------------------------------------------------------
# break — exit a loop early
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

# ---------------------------------------------------------------------------
# continue — skip a specific iteration (skip .100 in this example)
subnet = '192.168.1.'
ip_addresses = []
i = 0

while i < 256:
    i += 1
    if i == 100:
        continue
    ip_addresses.append(subnet + str(i))  # fixed: was append(subnet, str(i))

for ip in ip_addresses:
    print(ip)

# ---------------------------------------------------------------------------
# while/else — else block runs when the condition becomes False naturally
# (it does NOT run if the loop exited via break)
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
