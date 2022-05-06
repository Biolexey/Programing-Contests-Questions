n, t = map(int, input().split())
T = [*map(int, input().split())]
x = 0
for i in range(1, n):
    x += min(T[i]-T[i-1], t)
print(x+t)