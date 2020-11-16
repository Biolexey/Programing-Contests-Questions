from heapq import heappop, heappush
n = int(input())
path = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    path[a-1].append([b-1, c])
    path[b-1].append([a-1, c])

q, k = map(int, input().split())
d = [10**18]*n
d[k-1] = 0
hq = [(k-1, 0)]
gone = [0]*n
gone[k-1] = 1
while hq:
    node = heappop(hq)[0]
    for p, c in path[node]:
        if gone[p] == 0 and d[p] > d[node] + c:
            gone[p] = 1
            d[p] = d[node] + c
            heappush(hq, (p, d[p]))

for _ in range(q):
    x, y = map(int, input().split())
    print(d[x-1]+d[y-1])
