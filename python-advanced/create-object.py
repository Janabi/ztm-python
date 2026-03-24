class PlayerCharacter:
    membership = True # class object attribute (static attribute)
    # dunder methods
    def __init__(self, name='anonymous', age=0): # constructor method
        if self.membership:
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name} and I am {self.age} years old')

    @classmethod  # we can use it without creating an instance of the class
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod  # we don't care about class state or instance state
    def adding_things(num1, num2):
        return num1 + num2

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('AR', 33)
player2 = PlayerCharacter('John', 20)
print(player1)
print(player1.name)
print(player1.age)
print(player1.shout())
player1.run()

print(PlayerCharacter.membership)
print(player2.membership)

player1.speak = 'BOOOOO'
print(player1.speak)
# help(list)
# if you see underscore it means it's a private attribute
# player2 = { 'name': 'John', 'age': 20 }
# print(player2['name'])
# print(player2['age'])