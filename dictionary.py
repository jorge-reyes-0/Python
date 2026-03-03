sales = {
    'Jan': 2001,
    'Feb': 1412,
    'Mar': 3000,
    'Apr': 500,
    'May': 10000,
    'June': 100,
    'July': 679,
    'Aug': 301221,
    'Sep': 1,
    'Oct': 5,
    'Nov': 890,
    'Dec': 2320
}

highest = list(sales.values())[0]
highest_month = list(sales.keys())[0]

least = list(sales.values())[0]
least_month = list(sales.keys())[0]

total = 0
count = 0

for k in sorted(sales):
    print(k, sales[k])

    total += sales[k]
    count += 1

    if sales[k] > highest:
        highest = sales[k]
        highest_month = k

    if sales [k] < least:
        least = sales[k]
        least_month = k

average = total / count

print(f'The best sales month was {highest_month} with ${highest} in sales')
print(f'The worst sales month was {least_month} with ${least} in sales')
print(f'Total sales for the year is ${total}')
print(f'Average sales for 1 month was ${average}')