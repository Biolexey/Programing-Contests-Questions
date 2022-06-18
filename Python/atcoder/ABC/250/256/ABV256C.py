h1, h2, h3, w1, w2, w3 = map(int, input().split())

if h1+h2+h3 != w1+w2+w3:
    print(0)
    exit()
ans  =0
for i in range(w1+1):
    th1 = h1-i
    if th1 < 2:
        continue
    for j in range(w1+1-i):
        th2 = h2-j
        if th2 < 2:
            continue
        for k in range(w1+1-i-j):
            th3 = h3-k
            if th3 < 2:
                continue


"""
from numpy.linalg import solve

h1, h2, h3, w1, w2, w3 = map(int, input().split())

left = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
 
right = [h1, h2, h3, w1, w2, w3, 0, 0, 0]
 
print(solve(left, right))
"""