h, w = map(int, input().split())
s = [["."]+input().split()+["."] for _ in range(h)]
print(s)
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            continue
        else:
            if s[i][j+1] == "#" or s[i][j-1] == "#" or s[i-1][j] == "#" or s[i+1][j] == "#":
                continue
            else:
                print("No")
                exit()
print("Yes")