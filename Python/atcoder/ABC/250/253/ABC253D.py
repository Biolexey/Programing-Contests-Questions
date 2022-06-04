import math

n, a, b = map(int, input().split())
c = a*b//math.gcd(a, b)
na, nb, nc = n//a, n//b, n//c

gsum = n*(n+1)//2
asum = a*na*(na+1)//2
bsum = b*nb*(nb+1)//2
csum = c*nc*(nc+1)//2

print(gsum-asum-bsum+csum)