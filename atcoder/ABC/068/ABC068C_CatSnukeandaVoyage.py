n, m = map(int, input().split())
path = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)

for i in path[0]:
    if n-1 in path[i]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")