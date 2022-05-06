n, y = map(int, input().split())
for i in range(n+1):
    for j in range(n+1-i):
        k = n-i-j
        if 10*i + 5*j + k == y//1000 and 0 <= k <= 2000:
            print(i, j, n-i-j)
            exit()
print(-1, -1, -1)