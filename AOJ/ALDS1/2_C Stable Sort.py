n = int(input())
l = input().split()

def bubble(n, l):
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if l[j][1] < l[j-1][1]:
                l[j], l[j-1] = l[j-1], l[j]
    return l

def selection(n, l):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if l[j][1] < l[min][1]:
                min = j
        if min != i:
            l[min], l[i] = l[i], l[min]
    return l

x = l[:]
print(*bubble(n, l))
print("Stable")
print(*selection(n, x))
print("Stable" if x == l else "Not stable")
