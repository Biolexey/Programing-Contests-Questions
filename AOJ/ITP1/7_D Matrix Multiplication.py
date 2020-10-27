n, m, l = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(n)]
B = [[*map(int, input().split())] for _ in range(m)]
C = [0]*n
for i in range(n):
    li = []
    for j in range(l):
        ans = 0
        for k in range(m):
            ans += A[i][k]*B[k][j]
        li.append(ans)
    C[i] = li

for i in range(n):
    print(*C[i])