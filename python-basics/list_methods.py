basket = [1,2,3,4,5]
print(len(basket))

# adding
basket.append(100)
# inserting
basket.insert(5, 99)
# extend an existing list
basket.extend([101,102])

#removing at the end of the list by default
returned_removed_value = basket.pop()
basket.pop(0) # remove the first index
#removing based on a value
basket.remove(2)

print(basket)
print(basket.index(3, 0, 2))
print(1000 in basket)
print(basket.count(4))
print(returned_removed_value)
basket.clear()
print(basket)

alphabetic = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# alphabetic.sort()
print(sorted(alphabetic)) # it produces a new list
print(alphabetic)
new_alphabetic = alphabetic.copy()
new_alphabetic.reverse()
print(new_alphabetic)