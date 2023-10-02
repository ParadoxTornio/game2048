import time


def time_counter(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result

    return wrapper
