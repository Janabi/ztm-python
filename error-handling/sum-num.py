def sum_num(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        return 'please enter a valid number'
    except (TypeError, ZeroDivisionError) as err:
        return 'please enter a valid number'

print(sum_num(1, '2'))