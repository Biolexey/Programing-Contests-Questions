from collections import Counter
n = int(input())
A = Counter(map(int, input().split()))
A = {i: j for i, j in A.items() if j > 1}
if len(A) < 2:
    print(0)
else:
    A = sorted(A.items(), key=lambda x: -x[0])
    print(A[0][0]*A[1][0] if A[0][1] < 4 else A[0][0]*A[0][0])

