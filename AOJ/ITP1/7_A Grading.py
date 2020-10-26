while 1:
    n, f, r = map(int, input().split())
    sum = n + f
    if sum<0>r:
        break
    print("F" if (n*f<0) or (sum<30) else "D" if sum<50>r else "C" if sum<65 else "B" if sum<80 else "A")
    