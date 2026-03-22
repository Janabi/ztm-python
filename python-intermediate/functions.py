# Functions -> when you do a certain actions on a data types
# def -> means define a function
# DRY -> function used for writing the same code over and over, write once and call it everywhere
# Default parameters -> give a default value in case you haven't passed any argument
def say_hello(name = 'AR', emoji = '😅'): # parameters # positional 
    print(f'hellooooo {name} {emoji}')

# arguments -> actual values we provide to the function parameters
# positional arguments -> require to be in a proper position
say_hello('Janabi', '😎') # call, invoke

# keyword arguments
say_hello(emoji='😎', name='Janabi')
say_hello()
say_hello('programmer')

# return -> return some data type or None
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2) # return will exit the function
    # everything in the rest won't run
    print('Helloooo')
# Function
# should do something very well
# should return something

total = sum(10, 5)
print(sum(4,total))