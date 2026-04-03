import re

pattern = re.compile(r"([a-zA-Z]).([a])")

string = 'search inside of this text this please'

a = pattern.search(string)
print(a)

b = pattern.findall(string)
print(b)

c = pattern.fullmatch(string)
print(c)