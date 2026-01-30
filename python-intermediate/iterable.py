# iterable -> list, dictionary, tuple, set
# iterate -> one by one check each item in he collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for value in user.values():
    print(value)

for key in user.keys():
    print(key)

for key, value in user.items():
    print(key, value)