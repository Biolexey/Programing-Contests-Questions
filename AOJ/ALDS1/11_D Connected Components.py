n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

parent = [None] * n
for i in range(n):
    if parent[i] is None:
        parent[i] = i
        q = [i]
        while q:
            x = q.pop(0)
            for v in G[x]:
                if parent[v] is None:
                    parent[v] = i
                    q.append(v)

for _ in range(int(input())):
    s, t = map(int, input().split())
    print("yes" if parent[s] == parent[t] else "no")
