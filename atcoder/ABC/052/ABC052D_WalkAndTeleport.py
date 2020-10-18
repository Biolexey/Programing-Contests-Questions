n, a, b= map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    dx = a * (l[i+1] - l[i])
    if b < dx:
        ans += b
    else:
        ans += dx
print(ans)
