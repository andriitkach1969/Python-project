'''
Check Is number mathimatically simple
'''
import math, time


def findsimplenumber(number):
    if number>3:
        for currentnumber in range (3, number):
            r = range(2, int(math.sqrt(currentnumber)))
            for i in r:
                if currentnumber % i == 0:
                    break
            else:
                print("число ", currentnumber, " простое")

    else:
        print("введенное число - простое")

start_time = time.clock()

boundnumber = abs(int(input("Введите любое целое число: ")))
findsimplenumber(boundnumber)

line = 40*"="
print (line)
print (time.clock() - start_time, " seconds")
