h, w = map(int, input().split())
x, y = -1, -1
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "o":
            if x == -1:
                x = j
                y = i
            else:
                x = abs(j-x)
                y = abs(i-y)

print(x+y)
    