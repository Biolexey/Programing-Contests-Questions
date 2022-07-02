import math
mod = 998244353

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def fac(n):
    i = n
    while i>1:
        n *= i-1
        n %= mod
        i -= 1 
    return n

n = int(input())
n *= n
allnum = fac(n)%mod

sub = 0
for i in range(n, n*n+2-n):
    sub += cmb(i-1, n-1, mod)
    sub += cmb(n*n-i, n-1, mod)
print(sub)
print(allnum)

