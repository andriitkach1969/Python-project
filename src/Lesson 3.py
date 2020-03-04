def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

a = infinite_sequence()
print(next(a))


