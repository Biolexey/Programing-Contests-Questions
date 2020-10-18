n = int(input())
l = [*map(int, input().split())]
ls = sorted(l)

cost = 0
for cyc_min in range(n):
    i = l.index(ls[cyc_min])
    cyc = 0
    while i > cyc_min:
        cyc += 1
        i2 = l.index(ls[i])
        cost += l[i2]
        l[i], l[i2] = l[i2], l[i]
        i = i2
    cost += min(ls[cyc_min]*cyc, ls[cyc_min]*2 + ls[0]*(2 + cyc))

print(cost)