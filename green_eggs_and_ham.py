'''
green_eggs_and_ham.py: takes a Green Eggs and Ham story and corrects the
capitalization of 'i'. Based on https://redd.it/1i6sax
'''

import urllib.request

count = 0

def fixword(word):
    global count
    if word == 'i':
        word = 'I'
        count += 1
    elif 'Sam-i-am' in word:
        word = 'Sam-I-am'
        count += 1
    return word

def fixline(line):
    words = [fixword(word) for word in line.split()]
    return ' '.join(words) + '\n'

req = urllib.request.Request('http://pastebin.com/raw/XMY48CnN')
with urllib.request.urlopen(req) as f:
    with open('green_eggs_and_ham.txt', 'w') as f1:
        lines = [fixline(line.decode('utf-8')) for line in f]
        f1.writelines(lines)

print('Fixed', count, 'capitalization problems!')
