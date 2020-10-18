#自分の回答
n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n >= k:
    print(k*x + (n-k)*y)
else:
    print(n*x)

#ほかの回答
n = int(input())
k = int(input())
x = int(input())
y = int(input())
a = min(n,k)
print(a*k + (n-a)*y)