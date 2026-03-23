class User:
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self.num_arrows} arrows remaining')

    def run(self):
        print('ran really fast')

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
print(wizard1.sign_in())
print(wizard1.attack())

print(isinstance(wizard1, User))
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, Archer))
print(isinstance(wizard1, object))

archer1 = Archer('Robin', 100)
print(archer1.sign_in())
print(archer1.check_arrows())
print(archer1.run())