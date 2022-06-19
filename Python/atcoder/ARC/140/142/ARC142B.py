n = int(input())
ans = []

for i in range(n):
    ansl = [k for k in range(n*i+1, n*i+1+n)]
    if 0 < i < n-1:
        for j in range(n//2):
            tmp = ansl[2*j]
            ansl[2*j] = ansl[2*j+1]
            ansl[2*j+1] = tmp
        ans.append(ansl)
    else:
        ans.append(ansl)

for a in ans:
    print(*a)