''' pythagorean_triples.py: When given the sides of a triangle, tells the user
    whether the triangle is a right triangle. Based on https://www.redd.it/19jwi6 '''

while True:
    sides = input('Enter the three sides of a triangle, separated by spaces: ')
    try:
        sides = [int(x) for x in sides.split()]
    except ValueError:
        print('Error: please enter numbers only!')
    else:
        sides.sort()
        right = 'is' if (sides[0]**2 + sides[1]**2 == sides[2]**2) else 'is not'
        print('That {0} a right triangle.'.format(right))

    if input('Would you like to check another triangle? (Y/n) ').strip()[0].lower() == 'n':
        break;
