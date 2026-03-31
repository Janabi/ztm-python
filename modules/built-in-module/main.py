import random
# import random as r
# from random import random, randint, choice, shuffle

help(random)
print(dir(random))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice('hello'))
print(random.choice(['hello', 'world']))
print(random.choice(['hello', 'world']))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)