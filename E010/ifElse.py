input_year = int(input('Enter year: '))

if (input_year >= 601) and (input_year <= 700):
    print('The 7th century')
elif (input_year >= 701) and (input_year <= 800):
    print('The 8th century')
elif (input_year >= 801) and (input_year <= 900):
    print('The 9th century')
else:
    print('Not in the period of research')
