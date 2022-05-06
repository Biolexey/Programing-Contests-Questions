from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
n, m, r = map(int, input().split())
R = [*map(int, input().split())]
g = [[10**8]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = g[b][a] = c

g = floyd_warshall(g)

ans = []
for lst in permutations(R):
    ans += [sum([g[lst[i]][lst[i+1]] for i in range(0, r-1)])]

print(int(min(ans)))