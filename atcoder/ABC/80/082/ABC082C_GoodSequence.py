from collections import Counter
n = int(input())
c = Counter([*map(int, input().split())])
ans = 0
for i, j in c.items():
    if i <= j:
        ans += j-i
    else:
        ans += j
print(ans)