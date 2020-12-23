q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if abs(a-b) <= 1:
        print(2*min(a, b)-2)
    else:
        s = (a*b)**0.5
        if s == int(s):
            c = int(s)-1
        else:
            c = int(s)
        if c*(c+1) >= a*b:
            print(2*c-2)
        else:
            print(2*c-1)