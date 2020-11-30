from math import gcd
def lcm(x, y):
    return x*y//gcd(x, y)
n = int(input())
ans = int(input())
for _ in range(n-1):
    ans = lcm(int(input()), ans)
print(ans)