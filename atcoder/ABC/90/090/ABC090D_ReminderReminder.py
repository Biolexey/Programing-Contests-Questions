n, k = map(int, input().split())
ans = 0
if k == 0:
    print(n*n)
    exit()
for b in range(1, n+1):
    p, q = n//b, n%b
    ans += p*max(0, b-k) + max(0, q+1-k)
print(ans)