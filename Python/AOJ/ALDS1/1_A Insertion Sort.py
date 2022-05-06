n = int(input())
l = list(map(int, input().split()))
for i in range(0,n):
    x = l[i]
    j = i - 1
    while j >= 0 and l[j] > l[j + 1]:
        #print(str(l[j])+"のほうが"+str(l[j+1])+"より大きい")
        l[j + 1] = l[j]
        j -= 1
        l[j + 1] = x
        print(" ".join(list(map(str,l))))