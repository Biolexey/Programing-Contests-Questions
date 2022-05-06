import math
n, h = map(int, input().split())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
a_max = max(A)
B.sort(reverse=1)
cnt = 0
for b in B:
    if b < a_max:
        break
    cnt += 1
    h -= b
    if h <= 0:
        print(cnt)
        exit()
cnt += math.ceil(h/a_max)
print(cnt)