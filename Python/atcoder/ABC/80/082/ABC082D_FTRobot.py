s = input()
x, y = map(int, input().split())
sl = s.split("T")
dx = [*map(len, sl[::2])]
dy = [*map(len, sl[1::2])]
nx = dx.pop(0)
ny = 0
dx.sort(reverse=True)
dy.sort(reverse=True)
for xx in dx:
    if x >= nx:
        nx += xx
    else:
        nx -= xx
for yy in dy:
    if y >= ny:
        ny += yy
    else:
        ny -= yy
print("Yes" if nx == x and ny == y else "No")