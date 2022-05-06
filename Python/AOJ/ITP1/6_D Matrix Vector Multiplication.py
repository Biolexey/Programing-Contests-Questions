#numpyを使うとTLEでした。ぴえん。
# import numpy as np
# n, m = map(int, input().split())
# A = np.array([[*map(int, input().split())] for _ in range(n)])
# x = np.array([int(input()) for _ in range(m)])
# for i in A.dot(x):
#     print(i)

#numpy使わない書き方
n, m = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(n)]
x = [int(input()) for _ in range(m)]
for i in range(n):
    print(sum([(A[i][j]*x[j]) for j in range(m)]))