def res(num):
    try:
        r = 1/num
    except ZeroDivisionError as e:
        print('Exception error', e)
        return
    except Exception as e:
        print('Common Exception error', e)
        return
    finally:
        print('end try-except block')
        return r



if __name__ == "__main__":
    print(res(5))