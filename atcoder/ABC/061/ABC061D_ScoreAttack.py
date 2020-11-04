#辺の値を反転させて最短経路問題としてベルマンフォード法を用いた
n, m = map(int, input().split())
dist = [float("inf")]*n
dist[0] = 0
roop = [False]*n
edge = [[*map(int, input().split())] for _ in range(m)]
for j in range(n):
    for i in range(m):
        a, b, c = edge[i]
        c *= -1
        if roop[a-1] == True:
            roop[b-1] = True
        preb = dist[b-1]
        dist[b-1] = min(dist[a-1]+c, dist[b-1])
        if j == n-1:
            if preb != dist[b-1]:
                roop[b-1] = True

print("inf" if roop[n-1] else -dist[n-1])
