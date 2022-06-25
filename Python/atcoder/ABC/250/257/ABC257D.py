import math

n = int(input())
j = list(list(map(int, input().split())) for _ in range(n))
dist = []
N = []

maxnum = 0
maxidx = 0
for i in range(n):
    x1, y1, p = j[i][0], j[i][1], j[i][2]
    num = -1
    m = 0
    for k in range(n):
        if i == k:
            continue
        else:
            x2, y2 = j[k][0], j[k][1]
            d = math.sqrt((x1-x2)**2+(y1-y2)**2)/p
            if d > m:
                num = k
                m = d
            else:
                continue
    dist.append(m)
    print(num)
    N.append(num)

print(dist, N)