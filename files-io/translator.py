from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./files-io/test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./files-io/test-ja.txt', mode='w') as my_file:
            my_file.write(translation)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
finally:
    my_file.close()