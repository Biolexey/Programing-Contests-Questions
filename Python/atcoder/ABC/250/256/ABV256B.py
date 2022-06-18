n = int(input())
A = list(map(int, input().split()))
ans = [0]*4
p = 0

for a in A:
    ans[0] = 1
    p += ans[4-a:].count(1)
    for j in range(4-a, 4):
        if j <= 4-1:
            ans[j] = 0
    for i in range(0, 4-a)[::-1]:
        if 0 <= i <= 4-1:
            ans[i+a] = ans[i]
            ans[i] = 0
print(p)