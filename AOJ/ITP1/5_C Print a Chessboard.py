while 1:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        for j in range(w):
            if i%2 == 1:
                print("#" if j%2 == 1 else ".", end = "")
            else:
                print("#" if j%2 == 0 else ".", end = "")
        print()
    print()