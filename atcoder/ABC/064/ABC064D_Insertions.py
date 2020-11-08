n = int(input())
s = input()
d = []
l, r = 0, 0
for i in range(n):
    if s[i] == "(":
        l += 1
    else:
        r += 1
    d.append(l-r)
x = min(min(d), 0)
print("("*(-x) + s + ")"*(d[-1]-x))