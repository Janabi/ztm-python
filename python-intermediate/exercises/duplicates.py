some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
char_match = {}
duplicates = []

for item in some_list:
    if char_match.get(item):
        duplicates.append(item)
    else:
        char_match[item] = item

print(duplicates)