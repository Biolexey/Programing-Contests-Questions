x, a, b = map(int, input().split())
print("delicious" if 0 >= b-a else "safe" if b-a <= x else "dangerous")