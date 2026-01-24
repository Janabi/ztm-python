# Conditional Logic
is_old = False
is_licensed = 5 # it will treat it as if it was a boolean value type like bool(5) in if condition

# Truthy and Falsy

if is_old and is_licensed:
    print('you are old enough to drive, and you have a license')
# elif is_licensed:
#     print('you can drive now!')
else:
    print('you are not of age')

print('okokok')