n = int(input())
P = [*map(int, input().split())]+[n+10]
ans = 0
for i in range(n+1):
    if i+1 == P[i]:
        P[i], P[i+1] = P[i+1], P[i]
        ans += 1
print(ans)
