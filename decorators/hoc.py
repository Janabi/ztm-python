# Higher Order Function HOC
# A function that returns a function

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func

greet2()