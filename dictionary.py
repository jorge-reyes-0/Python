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
count = 0

for k in sorted(stats):
    print(k, stats[k])

    total += stats[k]
    count += 1

    if stats[k] > highest:
        highest = stats[k]
        highest_key = k

    if stats[k] < lowest:
        lowest = stats[k]
        lowest_key = k

average = total / count

print(f'Highest: {highest_key} {highest}')
print(f'Lowest: {lowest_key} {lowest}')
print(f'Total: {total}')
print(f'Average: {average}')