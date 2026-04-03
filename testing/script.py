import random

answer = random.randint(1, 10)
def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                return True
    except ValueError:
        return False
    return False

if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number: '))
            if run_guess(guess, answer):
                print('you are genius!')
                break
        except ValueError:
            print('please enter a number')
            continue

# print(run_guess(5, 5))