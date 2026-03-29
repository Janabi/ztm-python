try:
    age = int(input('what is your age?'))
    if int(age) < 18:
        print('you are not old enough')
    else:
        print('you are old enough')
    # raise Exception('you are not old enough')
except ValueError:
    print('please enter a valid age')
except ZeroDivisionError:
    print('please enter a valid age')
except TypeError:
    print('please enter a valid age')
except KeyboardInterrupt:
    print('please enter a valid age')
except EOFError:
    print('please enter a valid age')
finally:
    print('finally')