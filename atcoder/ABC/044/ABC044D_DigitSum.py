#自分の回答
import math
def digit(b, n):
    if n < b:
        return n
    else:
        return digit(b, math.floor(n/b)) + n % b

n, s = int(input()), int(input())  

if n == s:
    print(n+1)
    exit()

if n < s:
    print(-1)
    exit()

for i in range(2, int(math.sqrt(n)) + 2):
    if digit(i, n) == s:
        print(i)
        exit()

for p in range(1,int(math.sqrt(n)))[::-1]:
    q = s - p
    b = (n-s)//p +1
    if 1 <= p < b and 0 <= q < b and (n - s)%p == 0:
        if digit(b, n) == s:
            print(b)
            exit()
print(-1)    


