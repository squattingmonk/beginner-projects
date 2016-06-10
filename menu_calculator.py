'''
menu_calculator.py: Allows the user to enter the numbers of items ordered from
a menu and prints the total cost of the ordered items.

Based on https://redd.it/1bytu5
'''

from collections import Counter

menu = (('Chicken Strips', 3.50),
        ('Hamburger', 4.00),
        ('Hotdog', 3.50),
        ('Salad', 3.75),
        ('French Fries', 2.50),
        ('Large Drink', 1.75),
        ('Medium Drink', 1.50),
        ('Small Drink', 1.25),
        ('Milk Shake', 2.25))

while True:
    # Print the menu
    for index, (item, price) in enumerate(menu):
        print(index + 1, item.ljust(15), '${:,.2f}'.format(price))

    # Get the customer's order
    while True:
        try:
            order = input('Enter the items the customer is ordering: ')
            int(order)
            print()
            break
        except ValueError:
            print('Error: please enter integers only!\n')

    # Total up the value of the order
    total = 0
    for item, count in Counter(order).most_common():
        item = int(item) - 1
        per = menu[item][1]
        cost = per * count
        total += cost
        print(menu[item][0].ljust(15), count, '@', '${:3.2f}'.format(per),
                '\t$' + '{:.2f}'.format(cost).rjust(5))

    print('-' * 38)
    print('Total', '${:,.2f}'.format(total).rjust(32))

    # Ask if the user wants to try again
    try:
        if input('\nEnter another order? (Y/n) ').strip()[0].lower() == 'n':
            break
        else:
            print()
    except IndexError:
        print()
