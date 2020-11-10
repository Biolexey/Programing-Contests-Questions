n = int(input())
num = [*map(int, input().split())]
mod = 10**9+7
d = 0
for i in range(1, n+1):
    if num.count(i) == 2:
        d = i
        break
dup = [i for i, x in enumerate(num) if x == d]
l, r = dup[0]+1, dup[1]

lim = 1000
fac = [1]*(lim+1)
for i in range(1, lim+1):
    fac[i] = (fac[i-1]*i)%mod

print(fac)

for k in range(1, n+2):
    print(fac[n+1]//(fac[k]*fac[n+1-k]) - fac[l-1+n-r]//(fac[k-1]*fac[l+n-r-k]))
