from collections import Counter
n, k = map(int,input().split())
d = sorted(Counter([*map(int, input().split())]).values())
ans = 0
for i in range(len(d)-k):
    ans += d[i]
print(ans)
