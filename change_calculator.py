""" Change calculator: calculates the change in currency and coins owed to a
    customer. Based on https://redd.it/19jkn8 """

def make_change(amount):
    change = []

    for value in (100, 25, 10, 5, 1):
        change.append(amount // value)
        amount %= value

    return change

if __name__ == "__main__":
    while True:
        cost  = float(input("\nHow much does the item cost? $"))
        given = float(input("How much did the customer give you? $"))

        if cost > given:
            print("Oops! The customer did not give you enough money!")
        else:
            amount = int((given - cost) * 100)
            print("You need to give back {0} dollars, {1} quarters, {2} dimes, {3} nickels, and {4} pennies.".format(*make_change(amount)))
        
        if input("Would you like to do another transaction? (Y/n) ").lower() == "n":
            break;
