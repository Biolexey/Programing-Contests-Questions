n = int(input())
station = [[*map(int, input().split())] for _ in range(n-1)]
for i in range(n-1):
    t = 0
    for j in range(i, n-1):
        c, s, f = station[j][0], station[j][1], station[j][2]
        if t <= s:
            t = s+c
        elif (t-s)%f == 0:
            t += c
        else:
            t +=f - (t-s)%f + c
    print(t)
print(0)