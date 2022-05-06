n = int(input())
a = [0]+[*map(int, input().split())]+[0]
S = sum(abs(a[i]-a[i-1]) for i in range(1, n+2))
for i in range(1, n+1):
    print(S-abs(a[i]-a[i-1])-abs(a[i+1]-a[i])+abs(a[i-1]-a[i+1]))