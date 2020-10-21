n = int(input())
ans = 1
for i in range(1, n+1):
    ans = ans * i % (10**9+7)
print(ans%(10**9+7))

import math
n = int(input())
print(math.factorial(n) % (10**9+7))