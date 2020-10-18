import itertools
n, ma, mb = map(int, input().split())
l = list()
for _ in range(n):
    l.append(list(map(int, input().split())))
aset = set()
for i in range(1, n+1):
    l1 =  list(sum(itertools.combinations(l,i)))
    print(l1)
    #aset |= set(l1)

#print(aset)