import bisect, math
n = int(input())
a = sorted([*map(int, input().split())])
maxnum = a[-1]
a = a[:-1]
print(maxnum, min(a, key=lambda x: abs(maxnum-2*x)))