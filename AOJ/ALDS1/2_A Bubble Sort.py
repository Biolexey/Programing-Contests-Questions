n = int(input())
count = 0
l = list(map(int, input().split()))

for i in range(n):
    for j in reversed(range(i+1,n)):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            count += 1

print(*l)
print(count)
