#TLE(liをリストで実装するとTLE)
li = {}
n = int(input())
for _ in range(n):
    a = int(input())
    if a in li:
        del li[a]
    else:
        li[a] = 1
print(len(li))

#別解
from collections import Counter
import sys
import collections
n = int(input())
c = Counter(sys.stdin.readlines())
print(sum(v%2 for v in c.values()))
