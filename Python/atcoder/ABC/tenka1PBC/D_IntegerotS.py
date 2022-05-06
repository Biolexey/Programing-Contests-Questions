n, k = map(int, input().split())
num = [[*map(int, input().split())] for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j - num[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j-num[i-1][0]]+num[i-1][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
