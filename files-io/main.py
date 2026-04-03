my_file = open('./files-io/test.txt')
print(my_file.read())
my_file.seek(0) # move the cursor to the beginning of the file
print(my_file.readline())

my_file.close() # close the file after you are done with it

# with statement is a context manager that will automatically close the file after you are done with it
try:
    with open('./files-io/test.txt') as my_file:
        print(my_file.read())
        my_file.seek(0)
        print(my_file.readline())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
finally:
    my_file.close()

# write to a file
with open('./files-io/test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text)

# append to a file
with open('./files-io/happy.txt', mode='a') as my_file:
    text = my_file.write('I am happy!')
    print(text)