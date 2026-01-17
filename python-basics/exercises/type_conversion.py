from datetime import datetime

name = 'AR Janabi'
age = 33
relationship_status = 'single'

relationship_status = 'it\'s single'

print(relationship_status)

birth_year = input('what year you were born?')
age = datetime.now().year - int(birth_year)
# try this one: age = datetime.now().year - float(birth_year)
# try this one: age = datetime.now().year - bool(birth_year)
print(f'your age is {age}')