n = int(input())
s = [[0]*n for _ in range(n)]
for _ in range(n):
    u, k, *v = map(int, input().split())
    for x in v:
        s[u-1][x-1] = 1

for i in s:
    print(*i)