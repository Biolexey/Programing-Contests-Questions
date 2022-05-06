n = int(input())
l = list(map(int, input().split()))
count = 0
for i in range(n):
    min = i
    for j in range(i+1,n):
        if l[j] < l[min]:
            min = j
    if min != i:
        l[min], l[i] = l[i], l[min]
        count += 1

print(*l)
print(count)