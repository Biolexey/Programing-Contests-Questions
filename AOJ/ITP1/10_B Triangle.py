import math as ma
a, b, c = map(int, input().split())
S = a*b*ma.sin(c*ma.pi/180)/2
L = ma.sqrt(a**2 + b**2 - 2*a*b*ma.cos(ma.radians(c)))+a+b
h = 2*S/a
print(f"{S}\n{L}\n{h}")