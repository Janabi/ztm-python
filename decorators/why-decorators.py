from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'It took {end_time - start_time} seconds')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()