r, c = map(int, input().split())
ss = [0]*(r+1)
for i in range(r):
    ss[i] = [*map(int, input().split())]

for i in range(r):
    ss[i].append(sum(ss[i]))

lastli = []
for i in range(c+1):
    sum = 0
    for j in range(r):
        sum += ss[j][i]   
    lastli.append(sum)

ss[r] = lastli
for i in range(r+1):
    print(*ss[i])
    