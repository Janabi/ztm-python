# Sets
# a collection of unique objects
my_sets = {1,2,3,4,5,5}
my_sets.add(100)
my_sets.add(2)
print(my_sets)

my_lists = [1,2,3,4,5,5]
print(set(my_lists))

print(1 in my_sets)
print(len(my_sets))
new_set = my_sets.copy()
print(new_set)
