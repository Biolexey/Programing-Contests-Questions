n = int(input())
l = [input().split() for _ in range(n)]

def quicksort(l, p, r):
    if p < r:
        q= partition(l, p, r)
        quicksort(l, p, q-1)
        quicksort(l, q+1, r)

def partition(l, p, r):
    x = int(l[r][-1])
    i = p-1
    for j in range(p, r):
        if int(l[j][-1]) <= x:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1] ,l[r] = l[r], l[i+1]
    return i+1

l_sorted = sorted(l, key = lambda x: x[-1])
quicksort(l, 0, n-1)
print("Stable" if l == l_sorted else "Not stable")
for i in l:
    print(*i)
