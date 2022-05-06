n = int(input())
min = 10**9
ans = -10**9
for i in range(n):
    a = int(input())
    if i >= 1:
        ans = max(ans, a-min)
    if a < min:
        min = a

print(ans)
    