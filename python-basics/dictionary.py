# Dictionary
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4,5,6],
    'b': 'hello',
    'x': True
    }
]

print(my_list[1]['b'][1])
print(dictionary['a']) # will get the value of key 'b'
print(dictionary) # unordered key value pair