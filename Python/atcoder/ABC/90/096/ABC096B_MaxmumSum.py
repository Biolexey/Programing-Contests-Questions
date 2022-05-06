num = sorted([*map(int, input().split())], reverse=1)
k = int(input())
print(num[0]*2**k+sum(num[1:]))