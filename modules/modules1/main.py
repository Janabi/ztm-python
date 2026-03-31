# import utility
from utility import multiply, divide, add, subtract, Student
# import shopping.shopping_cart
from shopping.shopping_cart import buy

print(multiply(10, 20))
print(divide(10, 20))
print(add(10, 20))
print(subtract(10, 20))
print(buy('apple'))
print(__name__)
if __name__ == '__main__':
    print('please run this')

print(type(Student('AR', 33)))