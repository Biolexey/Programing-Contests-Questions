import sys

input = sys.stdin.readline
Q = int(input())
numdict = dict()

for _ in range(Q):
    q = list(input().split())
    if len(q) == 2:
        x = int(q[1])
        if x not in numdict:
            numdict[x] = 1
        else:
            numdict[x] += 1
    
    elif len(q) == 3:
        x, c = int(q[1]), int(q[2])
        if x in numdict:
            if numdict[x] <= c:
                numdict.pop(x)
            else:
                numdict[x] -= c
    
    else:
        print(max(numdict)-min(numdict))