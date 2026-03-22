print(range(0, 100))

for number in range(0, 10):
    print(number)

# when you use an underscore as a variable, then you don't care about its value you just need an iteration
for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -2):
    print(_)

for _ in range(2):
    print(list(range(10)))