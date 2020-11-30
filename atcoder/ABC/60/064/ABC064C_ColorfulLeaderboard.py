n = int(input())
rates = [*map(int, input().split())]
colors = []
cnt = 0
for rate in rates:
    color = "x"
    if 1 <= rate <= 399:
        color = "grey"
    elif 400 <= rate <= 799:
        color = "brown"
    elif 800 <= rate <= 1199:
        color = "green"
    elif 1200 <= rate <= 1599:
        color = "sky"
    elif 1600 <= rate <= 1999:
        color = "blue"
    elif 2000 <= rate <= 2399:
        color = "yellow"
    elif 2400 <= rate <= 2799:
        color = "orange"
    elif 2800 <= rate <= 3199:
        color = "red"

    if color == "x":
        cnt += 1
    else:
        colors.append(color)
colors = set(colors)
if len(colors) == 0:
    min = 1
else:
    min = len(colors)

max = len(colors) + cnt

print(min, max)

#リストを使って管理
n = int(input())
color = [0] * 9
a = list(map(int,input().split()))
for i in range(n):
    if a[i] < 3200:
        color[a[i]//400] = 1
    else:
        color[8] += 1
ansmin = sum(color[:8]) if sum(color[:8]) > 0 else 1
ansmax = sum(color[:8]) + color[8]
print(f"{ansmin} {ansmax}")
