#実際はmath.fanc使うよりも階乗求める際に逐次mod取った方が高速
import math
n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
mod = 10**9+7
if n - m > 1:
    print(0)
    exit()

if n - m == 0:
    print((math.factorial(n)%mod*2*math.factorial(m)%mod)%mod)
else:
    print((math.factorial(n)%mod*math.factorial(m)%mod)%mod)