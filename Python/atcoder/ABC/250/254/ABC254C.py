import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = sorted(a1)
idx = dict()

if a1 == a2:
    print("Yes")
    exit()

for a in range(n):
    if a1[a] not in idx:
        idx[a1[a]] = [a]
    else:
        idx[a1[a]].append(a)

for i in range(n):
    D = idx[a2[i]]
    ans = False
    for j in D:
        if (j-i)%k == 0:
            ans = True
            break
    if not ans:
        print("No")
        exit()

print("Yes")
