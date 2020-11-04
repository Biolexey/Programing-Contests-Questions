import math
a, b, c, d = map(int, input().split())
a -= 1
lcm = (c*d)//math.gcd(c,d)
A = a-(a//c+a//d-a//lcm)
B = b-(b//c+b//d-b//lcm)
print(B-A)