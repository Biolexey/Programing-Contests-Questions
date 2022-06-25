n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
num = [0]*k
i = 0

for a in A:
    num[i] = a
    i += 1

for l in L:
    if l == k:
        if num[l-1] == n:
            continue
        else:
            num[l-1] += 1
    else:
        if num[l] > num[l-1]+1:
            num[l-1] += 1
        else:
            continue
print(*num)
