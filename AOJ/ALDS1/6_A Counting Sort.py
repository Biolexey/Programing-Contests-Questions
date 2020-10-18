from collections import Counter
n = int(input())
s = [*map(int, input().split())]
c = dict(Counter(s))
l = [0]*(max(s)+1)
for key, item in c.items():
    l[key] = item
k = l[0]
for i in range(1, max(s)+1):
    l[i] += k
    k = l[i]
ans = list(0 for _ in range(n))
for i in reversed(s):
    ans[l[i]-1] = i
    l[i] -= 1
print(*ans)

#accumurateを使う
import itertools as it

n = int(input())
A = [*map(int, input().split())]

C = [0] * (max(A) + 1)
for a in A:
  C[a] += 1
C = [*it.accumulate(C)]

B = [None] * n
for a in reversed(A):
  C[a] -= 1
  B[C[a]] = a

print(*B)