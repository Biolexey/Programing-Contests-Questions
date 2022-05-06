n = int(input())
A = [None] * n
for _ in range(n):
    u, k, *V = map(int, input().split())
    A[u-1] = [v-1 for v in V]

g, r = [None]*n, [None]*n #GoとReturnのタイムスタンプ格納
t = 0

def dfs(x):
    global t
    t += 1
    g[x] = t
    for v in A[x]:
        if not g[v]:
            dfs(v)
    t += 1
    r[x] = t

for x in range(n):
    if not g[x]:
        dfs(x)
    print(x+1, g[x], r[x]) 