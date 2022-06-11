x, a, d, n = map(int, input().split())
n -= 1

if x < a:
    if d < 0:
        r = int(abs(x-a)/(-d))
        if r < n:
            #print("a")
            print(min(abs(x - a-d*r), abs(x - a-d*(r+1))))
        else:
            #print("b")
            print(abs(x- a-d*n))
    else:
        #print("c")
        print(a-x)

elif a < x:
    if d > 0:
        r = int(abs(x-a)/d)
        if r < n:
            #print("d")
            print(min(abs(x - a-d*r),abs(x - a-d*(r+1))))
        else:
            #print("e")
            print(abs(x- a-d*n))
    else:
        #print("f")
        print(x-a)

else:
    print(0)