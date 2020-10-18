def max_heapify(A, i):
    a = {j: A[j] if j < n else -float("inf") for j in [i, 2*i+1, 2*i+2]}
    i_max = max(a, key = a.get)
    if i != i_max:
        A[i], A[i_max] = A[i_max], A[i]
        max_heapify(A, i_max)

n = int(input())
s = [*map(int, input().split())]
for i in reversed(range(n//2)):
    max_heapify(s, i)
print("", *s)

#モジュールを使う
from heapq import heapify

_, heap = input(), [-int(x) for x in input().split()]
heapify(heap)
print("", *[-x for x in heap])