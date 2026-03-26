my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
}

my_dict_2 = { k:v**2 for k,v in my_dict.items() }
print(my_dict_2)

my_dict_3 = { k:v**2 for k,v in my_dict.items() if v % 2 == 0 }
print(my_dict_3)