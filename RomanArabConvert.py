'''
Roman to Arab and Arab to Roman convertion
'''

ROMANSIGN = [{1: 'I', 4: 'IV', 5: 'V', 9: 'IX'}, {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
             {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'}, {1: 'M'}]


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def arabToRoman(number):
    if not isint(number):
        print("Not a Arab number")
        return
    if number > 0 and number < 4000:
        resultStr = ""
        print(number)
        digit = 0
        i = 0
        while True:
            digit = number % 10
            number = number // 10
            print("digit - ", digit)
            if digit != 0:
                tmpStr = ROMANSIGN[i].get(digit, '*')
                if tmpStr == '*':
                    tmpStr = ''
                    if digit in (1, 2, 3):
                        base = 1
                    elif digit in (6, 7, 8):
                        base = 5
                        digit = digit - base + 1
                    tmpStr = tmpStr + ROMANSIGN[i][base]
                    for j in range(1, digit):
                        tmpStr = tmpStr + ROMANSIGN[i][1]
                resultStr = tmpStr + resultStr
                if number == 0:
                    break
            i += 1
        print("this number in Roman notation is: ", resultStr)
    else:
        print("Not a valid Arab number")


def romanToArab(arabstr):
    print(arabstr)


print("Convert number in Arab notation to Roman notation")
arabNumber = int(input("Enter any number in Arab notation (integer, >0 and < 4000): "))
arabToRoman(arabNumber)

print("Convert number in Roman notation to Arab notation")
romanStr = str(input("Enter any number in Roman notation: "))
romanToArab(romanStr)
