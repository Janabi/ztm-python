# Logical Operators
print(4 > 5)

print(4 == 5)
print('hello' == 'hello')

print('a' > 'A') # it is checking the unicode/ASCII point of these two character strings

print(1 < 2 > 3 < 5)
print(1 >= 0)
print(1 <= 0)
print(0 != 0) # check if they are do not equal

print(not(True))

# "==" check the equality of values (even if they were a different type)
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# "is" it is a keyword in python where it checks the both values are in the same location in memory
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])