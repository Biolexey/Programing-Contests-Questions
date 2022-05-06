import itertools
n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
aset = set()
for i in range(1, len(a)+1):
    aset |= set(sum(combi) for combi in itertools.combinations(a, i))

for j in m:
    print("yes" if j in aset else "no")