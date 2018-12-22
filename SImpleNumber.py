import math
import time


def issimple(number):
    if number in (1, 2, 3):
        return True
    else:
        bound = int(math.sqrt(number)) + 1
        r = range(2, bound)
        for j in r:
            if number % j == 0:
                break
        else:
            return True
        return False


'''
main module
'''
start_time = time.clock()

boundnumber = abs(int(input("Введите любое целое число больше нуля: ")))
if boundnumber > 0:
    for i in range(1, boundnumber+1):
        if issimple(i):
            print("простое -", i)
line = 40*"="
print(line)
print(time.clock() - start_time, " seconds")
