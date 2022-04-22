N = int(input())
 
a = 0
b = 1000000
X = 1 << 62
cnt = 0
while a <= b:
    tmp = a*a*a + a*a*b + a*b*b + b*b*b
    if tmp >= N:
        b -= 1
        X = min(X, tmp)
        
    else:
        a += 1
print(X)