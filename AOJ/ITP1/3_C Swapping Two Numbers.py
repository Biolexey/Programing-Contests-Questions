while 1:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        x, y = y, x
    print(x, y)