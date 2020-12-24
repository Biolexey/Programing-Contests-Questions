n, m, x = map(int, input().split())
a = [*map(int, input().split())]
i = 0
a1 = []
while a[i] < x:
    a1.append(i)
    i += 1
print(min(len(a1), len(a)-len(a1)))