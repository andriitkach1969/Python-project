initWeight = 50
endWeight = 1000
stepWeight = 50
priceStr = input('Please enter the price: ')
try:
    price = int(priceStr)
    try:
        for i in range(initWeight, endWeight + stepWeight, stepWeight):
            print(i, i / 1000 * price)
    except Exception as e:
        print('** Error. Something goes wrong \n', e)
except Exception as e:
    print('** Error. Your entered not a valid integer number \n', e)

