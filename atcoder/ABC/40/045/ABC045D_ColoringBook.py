#自分の回答(計算量がO(N^2)でTLEとなった)
h, w, n = map(int,input().split())
cell = [[0]*w for _ in range(h)]
for _ in range(n):
    a, b = map(int,input().split())
    cell[a-1][b-1] = 1

ans = [0]*10

for i in range(h-2):
    for j in range(w-2):
        s = [cell[i][j],cell[i+1][j],cell[i+2][j],cell[i][j+1],cell[i+1][j+1],cell[i+2][j+1],cell[i][j+2],cell[i+1][j+2],cell[i+2][j+2]].count(1)
        ans[s] += 1

for i in ans:
    print(i)

#解説読後に改めて書いたもの(これでも制限時間オーバーしてしまった)
h, w, n = map(int,input().split())
cell = [[0]*w for _ in range(h)]
for _ in range(n):
    a, b = map(int,input().split())
    for i in range(3):
        for j in range(3):
            if a-i>=0 and b-j>=0:
                cell[a-i-1][b-j-1] += 1
            else:
                continue

ans = [0]*10

for i in range(h-2):
    for j in range(w-2):
        s = cell[i][j]
        ans[s] += 1

for i in ans:
    print(i)

#ほかの回答
h, w, n = map(int,input().split())
 
xy_pos = dict()
 
for i in range(n):
    a, b = map(int, input().split())
    for k in range(-2,1):
        for l in range(-2,1):
            x = (a-1) + k
            y = (b-1) + l
            if (0 <= x <= h-3 and 0 <= y <= w-3):
                xy = str(x) + "x" + str(y)
                if xy in xy_pos:
                    xy_pos[xy] += 1
                else:
                    xy_pos[xy] = 1
 
ans = [0]*10                    
for v in xy_pos.values():
    ans[v] += 1
ans[0] = (h-2)*(w-2) - sum(ans)
for i in range(10):
    print(ans[i])
