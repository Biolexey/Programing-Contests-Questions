#自分の回答
import math
H, W, A, B = map(int, input().split())
count = 0
d = 10**9+7
for i in  range(H-A):
    count += (math.factorial(H+W-i-B-2)%d//(math.factorial(H-i-1)%d*math.factorial(W-1-B)%d)) * (math.factorial(B+i-1)%d//(math.factorial(B-1)%d*math.factorial(i)%d))
print(count)

# m=10**9+7
# h,w,a,b=map(int,input().split())
# d=c=1
# for i in range(h-1):
#     d=c=c*(w+h-b-2-i)*pow(i+1,m-2,m)%m
# for i in range(1,h-a):
#     c=c*(b-1+i)*(h-i)*pow(i*(w+h-b-1-i),m-2,m)%m
#     d+=c
# print(d%m)