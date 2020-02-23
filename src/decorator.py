from datetime import datetime


def time_delta(func):
    def function_wrapper(*args, **kwargs):
        _start_time = datetime.now()
        func(*args, **kwargs)
        _delta_time = datetime.now() - _start_time
        print('*** ' + func.__name__ + '\t\t. Call took a ', _delta_time)
    return function_wrapper


@time_delta
def f(st):
    print(st)


if __name__ == "__main__":
    f('F function call')
