n, stk = input().split()
rstk = stk[::-1]

n = int(n)
k = int(stk)
rk = int(rstk)

if stk[-1] == "0" or rstk[-1] == "0" or rk < k:
    print(0)
    exit()

if k == rk:
    p = 2
else:
    p = 1

l, h = min(rk, k), max(rk, k)

ans = 0

while 1:
    if l <= n:
        ans += 1
        l = l*10
    else:
        break
    if h <= n:
        ans += 1
        h = h*10
    else:
        break

print(ans//p)