def max_heapify(A, i):
    a = {j: A[j] if j < len(A) else -float("inf") for j in [i, 2*i+1, 2*i+2]}
    i_max = max(a, key = a.get)
    if i != i_max:
        A[i], A[i_max] = A[i_max], A[i]
        max_heapify(A, i_max)

def extract(A):
    print(A[0])
    A[0] = A[-1]
    A.pop()
    max_heapify(A,0)

def increase(A, i, key):
    A[i] = key
    while i and A[(i-1)//2] < A[i]:
        A[(i-1)//2], A[i] = A[i], A[(i-1)//2]
        i = (i-1)//2

def insert(A,key):
    A.append(None)
    increase(A, len(A)-1, key)

heap = list()
while True:
    op, *key = input().split()
    if op == "end":
        break
    if op == "extract":
        extract(heap)
    else:
        insert(heap, int(*key))

#上のやつではTLEになってしまったのでモジュールを使う
from heapq import heappop, heappush

heap = []
while True:
    op, *key = input().split()
    if op == "end":
        break
    if op == "extract":
        print(-heappop(heap))
    else:
        heappush(heap, -int(*key))