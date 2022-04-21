"""
N = int(input())

def num(n):
    if n == 1:
        return [1]
    elif n > 1:
        return num(n-1) + [n] + num(n-1)

print(*num(N))
"""
#DPでやってみる
N = int(input())
dp = [[] for _ in range(N+1)]
dp[1] = [1]
for n in range(2, N+1):
    dp[n] = dp[n-1] + [n] + dp[n-1]
print(*dp[N])