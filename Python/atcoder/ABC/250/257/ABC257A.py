a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x, y = map(int, input().split())
A = y//x-1
if y%x>0:
    B = 1
else:
    B = 0
print(a[A+B])