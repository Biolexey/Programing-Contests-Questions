h, w, d = map(int, input().split())
num = [0]*(h*w+1)
for i in range(h):
    for index, j in enumerate([*map(int, input().split())]):
        num[j] = [i, index+1]
D = [0]*(h*w+1)
for i in range(d+1, h*w+1):
    D[i] = D[i-d] + abs(num[i][0]-num[i-d][0]) + abs(num[i][1]-num[i-d][1])
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(D[r]-D[l])