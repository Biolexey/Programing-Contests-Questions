import math
n, a, b = map(int, input().split())
v = [*map(int, input().split())]
v.sort(reverse = True)

maxsum = 0
for i in range(a):
    maxsum += v[i]
maxave = maxsum/a
print(f"{maxave:.6f}")

va = v[:a]
if va[0] == va[a-1]:
    v0 = v.count(va[0])
    sum = 0
    for i in range(a, b+1):
        if v0-i >= 0:
            sum += int(math.factorial(v0)/(math.factorial(i)*math.factorial(v0-i)))
    print(sum)
else:
    v1 = va.count(va[a-1])
    v2 = v.count(va[a-1])
    print(int(math.factorial(v2)/(math.factorial(v1)*math.factorial(v2-v1))))