my_list = [1,2,3]
i = 0
while i < 50:
    print(i)
    i += 1
    break # else statement will not be executed
else:
    print('Done all of the work')

for item in my_list:
    print(item)
    break

j = 0
while j < len(my_list):
    j += 1
    continue
    print(my_list[j])

while True:
    response = input('say something: ')
    pass # placeholder while you are coding and it is nothing special to do
    if response == 'bye':
        break

