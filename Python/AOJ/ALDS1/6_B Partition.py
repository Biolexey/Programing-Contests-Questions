n = int(input())
l = [*map(int, input().split())]

def partition(l, p, r):
    x = l[r-1]
    i = p-1
    for j in range(p, r-1):
        if l[j] <= x:
            i += 1
            l[i], l[j] = l[j], l[i]
        print(l)
    l[i+1] ,l[r-1] = l[r-1], l[i+1]
    return i+1

c = partition(l, 0, n)
print(*l[:c], f"[{l[c]}]", *l[c+1:])