a = sorted([*map(int, input().split())])
print(a[0] if a[0] != a[1] else a[2])