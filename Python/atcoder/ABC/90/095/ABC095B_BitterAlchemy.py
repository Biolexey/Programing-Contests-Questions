n, x = map(int, input().split())
a = 1001
for _ in range(n):
    m = int(input())
    a = min(a, m)
    x -= m
print(n+x//a)