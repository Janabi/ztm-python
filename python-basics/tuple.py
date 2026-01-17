# Tuple
my_tuples = (1,2,3,4,5,6)
# Tuple cannot be modified once you created you cannot change any item then
# the remain would be the same as in the list
print(my_tuples[1])

dictionary = {
    (1,2): [1,2,3],
    'b': 'hello',
    'x': True
}

print(dictionary[(1,2)])

new_tuple = my_tuples[1:2]
print(new_tuple)

x,y,z, *other = my_tuples
print(x,y,z)
print(my_tuples.count(1))
print(len(my_tuples))