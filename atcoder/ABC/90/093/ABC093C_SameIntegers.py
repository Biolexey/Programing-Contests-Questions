num = [*map(int, input().split())]
ma = max(num)
if (3*ma)%2 == sum(num)%2:
    print((3*ma-sum(num))//2)
else:
    print(((3*(ma+1))-sum(num))//2)