#一応作ってみたがWA
n, k = map(int, input().split())
h = []
for _ in range(n):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == "W":
        y += k
    x %= 2*k
    y %= 2*k
    h.append([x, y])
ans = 0
for i in range(2*k+1):
    for j in range(2*k+1):
        cnt = 0
        for x, y in h:
            if j <= x <= min(j+k, 2*k) or 0 <= x <= max(0, j-k):
                if i <= y <= min(i+k, 2*k) or 0 <= y <= max(0, i-k):
                    cnt += 1 
        ans = max(ans, cnt)
print(ans)

#再考
n, k = map(int, input().split())
W = [[0]*(k+1) for _ in range(k+1)]
B = [[0]*(k+1) for _ in range(k+1)]
for _ in range(n):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if (x//k+y//k)&1:
        W[x%k+1][y%k+1]+=1 if c=='B' else 0
        B[x%k+1][y%k+1]+=1 if c=='W' else 0
    else:
        W[x%k+1][y%k+1]+=1 if c=='W' else 0
        B[x%k+1][y%k+1]+=1 if c=='B' else 0

for x in range(k+1):
    for y in range(k):
        W[x][y+1] += W[x][y]
        B[x][y+1] += B[x][y]

for y in range(k+1):
    for x in range(k):
        W[x+1][y] += W[x][y]
        B[x+1][y] += B[x][y]

ans = 0
for x in range(1, k+1):
    for y in range(1, k+1):
        cnt = 0
        cnt += B[k][k]-B[x][k]-B[k][y]+2*B[x][y]
        cnt += W[x][k]+W[k][y]-2*W[x][y]
        ans = max(ans, cnt, n-cnt)
print(ans)