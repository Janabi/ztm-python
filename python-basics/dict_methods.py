# Dictionary Methods
user = {
    'basket': [1,2,3],
    'greet': 'Hello',
    'age': 33
}

print(user.get('age', 20))

user2 = dict(name='AR')
print(user2)
print('age' in user2)
print('age' in user.keys())
print('Hello' in user.values())
print(user.items())

user_3 = user.copy()
user.clear()
print(user)
print(user_3)
print(user_3.popitem())
print(user_3)
print(user_3.update({ 'age': 34 }))
print(user_3.update({ 'ages': 44 }))
print(user_3)