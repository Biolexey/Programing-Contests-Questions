import math

n = int(input())

num = []
k = 1
while k <= n:
    num.append(k**2)
    k += 1
print(num)

cnt = 0
for K in num:
    for i in range(1, int(math.sqrt(K))+1):
        if i == math.sqrt(K):
            cnt += 1

        elif K%i == 0 and K/i <= k:
            cnt += 2

print(cnt)

"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

cnt = 1
k = 2
while k <= n:
    fac = factorization(k**2)
    print(k**2, fac)
    for i in fac:
        cnt += i[1]+1
    k += 1

print(cnt)
"""
