n = int(input())
num = [9,8,7,6,5,4,3,2,1]

A = list(list(input()) for _ in range(n))
cand = []

i =  0
for _  in range(n):
    M = 0
    for i in range(n):
        for j in range(n):
            if M < int(A[i][j]):
                M = int(A[i][j])
                cand = [(i, j)]
            elif M == int(A[i][j]):
                cand.append((i, j))
    
