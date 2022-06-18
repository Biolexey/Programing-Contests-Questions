n = int(input())
rng = [0]*(2*(10**5)+1)

for _ in range(n):
    x, y = map(int, input().split())
    rng[x] += 1
    rng[y] -= 1

en = 0
ans = 0
for i in range(len(rng)):
    if rng[i] > 0:
        en += rng[i]
        if ans == 0:
            ans = i
    if rng[i] < 0:
        en += rng[i]
        if en > 0:
            continue
        else:
            print(ans, i)
            ans = 0