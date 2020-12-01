#自分の回答
N = int(input())
t = x = y = 0
point = []
for i in range(N):
    array = list(map(int, input().split()))
    point.append(array)

for i in range(N):
    if (point[i][0]-t < abs(point[i][1]-x)+abs(point[i][2]-y)) or ((abs(point[i][1]-x)+abs(point[i][2]-y)+point[i][0]-t)%2 != 0):#tがx+yよりも小さい時、もしくはtとx+yの偶奇が一致していないとき
        print("No")
        exit()
    t = point[i][0]
    x = point[i][1]
    y = point[i][2]

print("Yes")

#簡潔(入力ごとに判定が行われる)
N = int(input())
t0 = x0 = y0 = 0
for i in range(N):
    t, x, y = map(int, input().split())
    if t - t0 < abs(x - x0) + abs(y - y0) or (t - t0 + abs(x - x0) + abs(y - y0)) % 2 != 0:
        print("No")
        exit()
    t0, x0, y0 = t, x, y
print("Yes") 

#簡潔(入力後一括で判定)
N = int(input())
t, x, y = 0, 0, 0
l = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    if l[i][0]-t >= abs(l[i][1]-x)+abs(l[i][2]-y) and (l[i][0]-t-abs(l[i][1]-x)+abs(l[i][2]-y)) % 2 == 0:
        t, x, y = l[i][0], l[i][1], l[i][2]
    else:
        print("No")
        break
else:
  print("Yes")
  
