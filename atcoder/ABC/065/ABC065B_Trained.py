n = int(input())
num = [int(input()) for _ in range(n)]
cnt = 0
next = 0
for _ in range(n):
    next = num[next]-1
    cnt += 1
    if next == 1:
        print(cnt)
        exit()
print(-1)

