import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
pl = list(list(map(int, input().split())) for _ in range(n))
dist = []
for i in pl:
    tmp = 10**9
    x, y = i[0], i[1]
    for j in a:
        tmp = min(tmp, math.sqrt((pl[j-1][0]-x)**2 + (pl[j-1][1]-y)**2))
    dist.append(tmp)
print(max(dist))