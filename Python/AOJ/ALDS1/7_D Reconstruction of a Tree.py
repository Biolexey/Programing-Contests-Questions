_ = int(input())
preo = [*map(int, input().split())]
ino = [*map(int, input().split())]
ans = []

def reconst(preo, ino):
    if preo:
        root = preo[0]
        i = ino.index(root)
        reconst(preo[1:i+1], ino[:i])
        reconst(preo[i+1:], ino[i+1:])
        ans.append(root)

reconst(preo, ino)
print(*ans)