# This is a match code block
# With a match, the expression is evaluated once
# The expression is compared with the values of each case
# If there is a match, the block of code is executed

day = 5
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case _:
        print('Not a match')

# You can use the pipe character to check for more than one value match in one case       

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print('Today is a weekday')
    case 6 | 7:
        print('This is a weekend')

# You can add if statements in the case evaluation as another condition check

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print('A weekday in April')
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print('A weekday in May')
    case _:
        print('No match')
