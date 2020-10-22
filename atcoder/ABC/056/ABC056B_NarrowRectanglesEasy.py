w, a, b = map(int, input().split())
if a <= b <= a+w or b <= a <= b+w:
    print(0)
    exit()
print(min(abs(b-a-w), abs(a-b-w)))