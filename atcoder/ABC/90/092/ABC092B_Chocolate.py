n = int(input())
d, x = map(int, input().split())
cnt = 0
for _ in range(n):
    cnt += (d-1)//int(input()) + 1
print(x+cnt)