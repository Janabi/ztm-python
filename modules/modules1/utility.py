print(__name__)

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

if __name__ == '__main__':
    print('please run this')

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age})'

    def __len__(self):
        return len(self.name)