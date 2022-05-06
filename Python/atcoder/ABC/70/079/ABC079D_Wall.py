from scipy.sparse.csgraph import floyd_warshall
h, w = map(int, input().split())
g = list(range(10))
for i in range(10):
    g[i] = [*map(int, input().split())]
g = floyd_warshall(g)
ans = 0
for _ in range(h):
    num = [*map(int, input().split())]
    for i in range(w):
        if num[i] == -1:
            continue
        else:
            ans += g[num[i]][1]
print(int(ans))

