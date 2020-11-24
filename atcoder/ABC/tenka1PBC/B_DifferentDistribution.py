n = int(input())
max = 0
l = 0
for _ in range(n):
    a, b = map(int, input().split())
    if max < a:
        l = b
        max = a
print(max+l)
