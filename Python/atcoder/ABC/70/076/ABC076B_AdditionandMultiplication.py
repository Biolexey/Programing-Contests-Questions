n, k = int(input()), int(input())
ans = 1
for _ in range(n):
    if ans <= k:
        ans *= 2
    else:
        ans += k
print(ans)