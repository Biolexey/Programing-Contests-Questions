a, b = map(int, input().split())
W = [["."]*100 for _ in range(50)]
B = [["#"]*100 for _ in range(50)]

def paint(color, cnt, G):
    for i in range(0,49,2):
        for j in range(0,100,2):
            if cnt == 1:
                return G
            if color == "w":
                G[i][j] = "."
            else:
                G[i][j] = "#"
            cnt -= 1

B = paint("w", a, B)
W = reversed(paint("b", b, W))
print(100, 100)
for i in B:
    print("".join(i))
for i in W:
    print("".join(i))