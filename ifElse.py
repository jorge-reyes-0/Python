num_things = int(input('Enter your number: '))

if num_things == 12:
    print('Dozen')
elif num_things == 13:
    print("Baker's Dozen")
elif num_things == 20:
    print('Score')
else:
    print('Name not found')
