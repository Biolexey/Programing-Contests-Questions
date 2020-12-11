n = int(input())
t, x, y = 0, 0, 0
l = [[*map(int, input().split())] for _ in range(n)]
for i in range(n):
    T, X, Y = l[i][0], l[i][1], l[i][2]
    if T-t >= abs(X-x)+abs(Y-y) and (T-t-abs(X-x)+abs(Y-y))%2 == 0:
        t, x, y = T, X, Y
    else:
        print("No")
        break
else:
    print("Yes")