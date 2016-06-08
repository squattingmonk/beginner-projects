'''
fibonacci.py: Prints the Fibonacci sequence to the limit specified by the user.
Uses a generator function for fun. Based on https://redd.it/19r3qg.
'''

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = None
    while n is None:
        try:
            n = int(input('How many numbers would you like to print? '))
        except ValueError:
            print('Error: Please enter integers only!')
            pass

    for i in fib(n):
        print(i, end=' ')

    print(' ')
