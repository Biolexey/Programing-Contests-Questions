q = int(input())
n = 10**5+1
p = [1]*n
d = [0]*n
p[0], p[1] = 0, 0
for i in range(2, int(n**0.5)):
    if p[i]:
        for j in range(i*2, n, i):
            p[j] = 0
cnt = 0
for i in range(1, n):
    if p[i] and p[(i+1)//2]:
        cnt += 1
    d[i] = cnt
for _ in range(q):
    l, r = map(int, input().split())
    print(d[r]-d[l-1])
