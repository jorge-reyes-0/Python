### Computes the total amount of minutes, after converting minutes and adding minutes from user input

hours = int(input('Enter hours:\n'))
minutes = int(input('Enter minutes:\n'))

hours_toMinutes = hours * 60
total_minutes = hours_toMinutes + minutes

print(total_minutes, 'minutes')