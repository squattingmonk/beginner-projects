'''
multiplication_table.py: prints a formatted multiplication
table for digits up to the number specified by the user.

Based on https://redd.it/2agwnq
'''

max_factor = None
while  max_factor is None:
    try:
        max_factor = int(input('What number would you like to multiply up to? '))
    except ValueError:
        print('Error: please enter integers only!')
        pass

max_length = len(str(max_factor ** 2)) + 1


for i in range(1, max_factor + 1):
    for j in range (1, max_factor + 1):
        print(str(i * j).rjust(max_length, ' '), end='')
    print()
