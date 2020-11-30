#自分の解答
n, k = map(int, input().split())
l = list(map(int, input().split()))
pay = n
while any(str(i) in str(pay) for i in l):
    pay += 1
print(pay)
