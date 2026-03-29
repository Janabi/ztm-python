def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(10):
    print(item)

def generator_function(num):
    for i in range(num):
        yield i*2

for item in generator_function(10):
    print(item)

# generator is a function that returns a generator object
# generator object is an iterable object
# generator object is a lazy object
# generator object is a memory efficient object
# generator object is a faster object
# generator object is a more readable object
# generator object is a more maintainable object
# generator object is a more scalable object
generator_function = generator_function(10)
print(generator_function)
print(next(generator_function))
print(next(generator_function))