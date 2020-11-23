import numpy as np
n = int(input())
a = np.array([[*map(int, input().split())] for _ in range(n)])
ans = 0
for i in range(n):
    a[i][i] = 10**9+1
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        dp = np.min(a[i]+a[j])#直接経路以外での最小経路
        if a[i][j] < dp:#その経路よりも短かったらそれが道路として存在する
            ans += a[i][j]
        elif a[i][j] > dp:#長かったらその長さは真の最短経路ではない。よって不適
            print(-1)
            exit()
#等しかったらdpの経路が最短経路であるとされる
print(ans)