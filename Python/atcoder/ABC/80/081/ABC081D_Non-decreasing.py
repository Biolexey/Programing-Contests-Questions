n = int(input())
a = [*map(int, input().split())]
ma, mi = max(a), min(a)
print(2*n-1)

if (ma*mi < 0 and -mi<ma) or mi>=0:
    ind = a.index(ma)+1
    for i in range(n):
        print(ind, i+1)
    for i in range(n-1):
        print(i+1, i+2)
else:
    ind = a.index(mi)+1
    for i in range(n):
        print(ind, i+1)
    for i in reversed(range(n-1)):
        print(i+2, i+1)