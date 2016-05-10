''' mean_median_mode.py: When given a list of numbers, prints the mean, median,
    and mode of the list. Based on https://www.redd.it/1eqt8i '''

from collections import Counter

def mean(numbers):
    '''Returns the mean of a list of numbers.'''
    return sum(numbers) / len(numbers)

def median(numbers):
    '''Returns the median of a given list of numbers.'''
    index = len(numbers) // 2
    numbers.sort()

    if len(numbers) % 2 == 1:
        return numbers[index]
    else:
        a, b = numbers[index - 1], numbers[index]
        return a if a == b else (a, b)

def mode(numbers):
    '''Returns the mode(s) of a given list of numbers.'''
    counts = Counter(numbers).most_common()
    return [val for val, count in counts if count == counts[0][1]]

if __name__ == '__main__':
    numbers = input('Please enter a list of numbers separated by spaces: ')

    try:
        numbers = [int(number) for number in numbers.split()]
    except ValueError:
        print('Error: please enter integers only!')
    else:
        message = 'The mean is {0}, the median is {1}, and the mode is {2}.'
        print(message.format(mean(numbers), median(numbers), mode(numbers)))
