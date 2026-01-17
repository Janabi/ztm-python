alphabetic = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(alphabetic[::-1])
print(alphabetic)

print(list(range(1, 100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'AR'])

print(new_sentence)

# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)