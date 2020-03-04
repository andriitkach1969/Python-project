def a(_a):
    print('in a()')
    return -_a


if __name__ == "__main__":
    if 3 == 5 and a(3) == -3:
        print('end')
    b = 0
#    assert b is None, 'Error in data'
