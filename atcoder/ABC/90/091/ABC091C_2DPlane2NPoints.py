n = int(input())
r = sorted([[*map(int, input().split())] for _ in range(n)], key = lambda x: x[1])[::-1]
b = sorted([[*map(int, input().split())] for _ in range(n)])
cnt = 0
for blue in b:
    c, d = blue
    for red in r:
        a, b = red
        if (a<c and b<d):
            cnt += 1
            r.remove([a, b])
            break
print(cnt)