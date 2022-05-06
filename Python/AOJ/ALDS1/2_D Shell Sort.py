def insertion(a, n, g):
    count = 0
    for i in range(g, n):
        ref = a[i]
        j = i - g
        while j >= 0 and ref < a[j]:
            a[j+g] = a[j]
            j -= g
            count += 1
        a[j+g] = ref
    return count

n = int(input())
a = [int(input()) for _ in range(n)]

m = int.bit_length(n)
print(m)
G = [n//(2**i) for i in range(m)]
print(*G)
print(sum(insertion(a, n, G[i]) for i in range(m)))
print(*a, sep = "\n")