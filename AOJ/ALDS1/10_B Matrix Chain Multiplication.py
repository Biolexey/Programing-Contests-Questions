#トップダウン
from functools import lru_cache

n = int(input())
p = [int(input().split()[0]) for _ in range(n-1)] + [*map(int, input().split())]
print(p)

@lru_cache(maxsize=None)
def n_mul(i, j):
  if j - i == 1:
    return 0
  return min(n_mul(i,k) + n_mul(k,j) + p[i]*p[k]*p[j] for k in range(i+1,j))

print(n_mul(0, n))

#ボトムアップ
n = int(input())
p = [int(input().split()[0]) for _ in range(n-1)] + [*map(int, input().split())]

dp = [[0]*(n+1) for _ in range(n+1)]
for l in range(2, n+1):#考える行列の個数
    for i in range(n-l+1):
        j = l+i
        dp[i][j] = min(dp[i][k] + dp[k][j] + p[i]*p[k]*p[j] for k in range(i+1, j))
    print(dp)
print(dp[0][n])