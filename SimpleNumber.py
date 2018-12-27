'''
stage 1
'''
import math
import time


def issimple(number):

    def check(_number):
        bound = int(math.sqrt(_number)) + 1
        r = range(2, bound)
        for j in r:
            if _number % j == 0:
                break
        else:
            return True
        return False

    route = {1: True, 2: True, 3: True}
    return route.get(number, check(number))


if __name__ == '__main__':
    start_time = time.clock()

    boundnumber = abs(int(input("Введите любое целое число больше нуля: ")))
    if boundnumber > 0:
        for i in range(1, boundnumber+1):
            if issimple(i):
                print("простое -", i)
    line = 40*"="
    print(line)
    print(time.clock() - start_time, " seconds")
