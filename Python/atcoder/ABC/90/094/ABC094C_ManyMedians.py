n = int(input())
x = [*map(int, input().split())]
sx = sorted(x)
a, b = sx[(n-2)//2], sx[n//2]
for i in x:
    print(a if i > a else b)
