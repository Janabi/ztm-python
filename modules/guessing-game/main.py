# guessing game by input through sys
import sys
import random
answer = random.randint(1, 10)

while True:
    try:
        guess = int(input('guess a number: '))
        if guess == answer:
            print('you are right!')
            break
    except ValueError:
        print('please enter a valid number')
        continue