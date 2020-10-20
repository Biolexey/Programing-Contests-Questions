from heapq import heapify, heappop

n = int(input())
s = [None]*n
for _ in range(n):
    u, k, *vc = map(int, input().split())
    s[u] = {vc[2*i]: vc[2*i+1] for i in range(k)}

d = [None]*n
heap = [[float("inf"), v] for v in range(n)]
heap[0] = [0, 0]
while heap:
    heapify(heap)
    du, u = heappop(heap)
    d[u] = du
    for i, [dv, v] in enumerate(heap):
        if v in s[u]:
            dv1 = du + s[u][v]
            if dv1 < dv:
                heap[i] = [dv1, v]

for x in range(n):
    print(x, d[x])