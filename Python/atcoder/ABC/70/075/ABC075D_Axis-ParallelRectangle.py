from itertools import combinations
n, k = map(int, input().split())
cor = sorted([[*map(int, input().split())] for _ in range(n)])
ans = float("inf")
for s, t in combinations(range(n), 2):
    x1, x2 = cor[s][0], cor[t][0]
    y = []
    for i in range(n):
        if x1 <= cor[i][0] <= x2:
            y.append(cor[i][1])
    y.sort()
    for i in range(len(y)-k+1):
        y1, y2 = y[i], y[i+k-1]
        s = (y2-y1)*(x2-x1)
        ans = min(ans, s)
print(ans)