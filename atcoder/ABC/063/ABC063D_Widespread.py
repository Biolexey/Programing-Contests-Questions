from math import ceil
n, a, b = map(int, input().split())
enemies = sorted([int(input()) for _ in range(n)])

def damage(x):
    cnt = 0
    for enemy in enemies:
        if enemy <= x*b:
            continue
        else:
            cnt += ceil((enemy-x*b)/(a-b))
    return cnt <= x

max, min = 10**9, 0
while abs(max-min)>1:
    mid = (max+min)//2
    if damage(mid):
        max = mid
    else:
        min = mid
print(max)
