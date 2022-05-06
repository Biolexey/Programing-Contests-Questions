#当然これではO(n^2m^2)なのでTLE
n, m = map(int, input().split())
X = [*map(int, input().split())]
Y = [*map(int, input().split())]
mod = 10**9+7

sum = 0
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(m-1):
            for l in range(k+1, m):
                sum += ((X[j]-X[i])%mod)*((Y[l]-Y[k])%mod)

print(sum%mod)

#因数分解したあと各項を和の形に直す
n, m = map(int, input().split())
X = [*map(int, input().split())]
Y = [*map(int, input().split())]
mod = 10**9+7

x = 0#xの和
for i in range(1, n+1):
    x += ((i-1)*X[i-1] - (n-i)*X[i-1])%mod

y = 0#yの和
for j in range(1, m+1):
    y += ((j-1)*Y[j-1] - (m-j)*Y[j-1])%mod

print(x*y%mod)
