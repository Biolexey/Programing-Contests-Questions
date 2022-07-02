num = sorted(list(map(int, input().split())))
base = num[0]
if num[2]-num[1] > base:
    print(-1)
else:
    print(num[2])
