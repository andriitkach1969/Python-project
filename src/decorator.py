def deco(func):
    def function_wrapper(x):
        print('Deco function')
        func(x)
    return function_wrapper


@deco
def f(st):
    print(st)


if __name__ == "__main__":
    f('F function call')
