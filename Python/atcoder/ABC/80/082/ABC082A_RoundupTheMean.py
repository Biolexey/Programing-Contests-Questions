import math
a, b = map(int, input().split())
print(math.ceil((a+b)/2))

#別解
a, b = map(int, input().split())
print((a+b+1)//2)