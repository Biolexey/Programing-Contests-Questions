a, b = map(int, input().split())
cnt = 0
for i in range(1, a+1):
    for j in range(1, 31):
        if i == j:
            cnt += 1
        if i == a and j == b:
            print(cnt)
            break
