h, w = map(int, input().split())
bomb = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if bomb[i][j] == "#":
            print("#", end="")
        else:
            cnt = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if i + y < 0 or i + y >= h:
                        continue
                    if j + x < 0 or j + x >= w:
                        continue
                    if bomb[i+y][j+x] == "#":
                        cnt += 1
            print(cnt, end="")
    print("\n", end="")
            