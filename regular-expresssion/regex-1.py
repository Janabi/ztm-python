import re

pattern = re.compile('this')

string = 'search inside of this text this please'

a = pattern.search(string)
print(a)

b = pattern.findall(string)
print(b)

c = pattern.fullmatch(string)
print(c)

d = pattern.match(string)
print(d)