#12_Bと同じだとTLE
from heapq import heappop, heappush
n = int(input())
s = [None]*n
for _ in range(n):
    u, k, *cv = map(int, input().split())
    s[u] = {cv[2*i]: cv[2*i+1] for i in range(k)}

d = [0] + [float("inf")]*(n-1)
heap = [[0,0]]
while heap:
    du, u = heappop(heap)
    for v in s[u]:
        dv = du + s[u][v]
        if d[v] > dv:
            d[v] = dv
            heappush(heap, [d[v], v])

for x in range(n):
    print(x, d[x])
