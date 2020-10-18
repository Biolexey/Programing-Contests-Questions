n, t = map(int, input().split())
a = list(map(int, input().split()))
count = 0
l = []
max = 0
min = a[0]
for i in range(1,n):
    if a[i] < min:
        min = a[i]
    if a[i] - min > max:
        max = a[i] - min
    l.append(a[i] - min)
print(l.count(max))