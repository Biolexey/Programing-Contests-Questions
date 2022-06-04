n = int(input())
l = [1]
for _ in range(n):
    print(*l)
    num = len(l)
    l.append(1)
    for i in range(num-1):
        if num > 1:
            l.append(l[i]+l[i+1])
    l = l[num:]
    l.append(1)
