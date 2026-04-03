import re

#password checker
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

string = 'okokOk123@okokOk'

a = pattern.search(string)
print(a)