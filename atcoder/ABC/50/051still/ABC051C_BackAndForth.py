sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy
print("U"*dy + "R"*dx, end="")
print("D"*dy + "L"*dx, end="")
print("L" + "U"*(dy+1) +"R"*(dx+1) +"D", end="")
print("R" + "D"*(dy+1) +"L"*(dx+1) +"U", end="")