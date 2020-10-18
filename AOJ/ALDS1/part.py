def partition(l, p, r):
    x = int(l[r-1][-1])
    i = p-1
    for j in range(p, r-1):
        if int(l[j][-1]) <= x:
            i += 1
            l[i], l[j] = l[j], l[i]
        print(l)
    l[i+1] ,l[r-1] = l[r-1], l[i+1]
    return i+1
