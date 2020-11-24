n = int(input())
for a in range(n//4+1, 3501):
    for b in range((n*a)//(4*a-n), 3501):
        if 4*a*b-n*b-n*a == 0:
            continue
        c = (n*a*b)/(4*a*b-n*b-n*a)
        if c == int(c) and c > 1:
            print(a, b, int(c))
            exit()
