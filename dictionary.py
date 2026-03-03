stats = {
    'Jan': 34,
    'Feb': 28,
    'Mar': 41,
    'Apr': 30
}

highest = list(stats.values())[0]
highest_key = list(stats.keys())[0]
lowest = list(stats.values())[0]
lowest_key = list(stats.keys())[0]
total = 0

for k in sorted(stats):
    print(k, stats[k])

    total += stats[k]

    if stats[k] > highest:
        highest = stats[k]
        highest_key = k

    if stats[k] < lowest:
        lowest = stats[k]
        lowest_key = k

print(f'Highest: {highest_key} {highest}')
print(f'Lowest: {lowest_key} {lowest}')
print(f'Total: {total}')