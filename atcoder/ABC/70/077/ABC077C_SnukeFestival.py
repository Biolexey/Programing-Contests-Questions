from bisect import bisect_left, bisect_right
n = int(input())
a = sorted([*map(int, input().split())])
b = sorted([*map(int, input().split())])
c = sorted([*map(int, input().split())])

ans = 0
for i in b:
    l = bisect_left(a, i)
    r = n - bisect_right(c, i)
    ans += l*r
print(ans)