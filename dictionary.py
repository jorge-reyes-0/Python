employees = {
    'Alice': 55,
    'Brian': 72,
    'Carla': 60,
    'David': 48
}

highest = 0
highest_key = ''
total = 0

for name in sorted(employees):
    print(name, employees[name])

    total += employees[name]

    if employees[name] > highest:
        highest = employees[name]
        highest_key = name

print(f'Most hours: {highest_key} {highest}')
print(f'Total hours: {total}')