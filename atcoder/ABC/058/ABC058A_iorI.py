a, b, c = map(int, input().split())
x = b - a
y = c - b
print("YES" if x == y else "NO")