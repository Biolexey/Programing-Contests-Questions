from typing import Deque


from collections import deque
n = int(input())
G = [None]*n
for _ in range(n):
    u, k, *V = map(int, input().split())
    G[u-1] = [v-1 for v in V]
d = [0] + [-1]*(n-1)
q = deque([0])

while q:
    v = q.popleft()
    for u in G[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)

for x in range(n):
    print(x+1, d[x])

