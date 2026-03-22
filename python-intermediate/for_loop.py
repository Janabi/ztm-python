for item in 'Zero to Mastery':
    print(item)

for item in {1,2,3,4,5}:
    print(item)

for item in (1,2,4,5,6):
    print(item)

for item in [1,2,4,5,6]:
    print(item)
print(item) # the item variable still consider as defined variable and it holds the last value

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)