from collections import Counter, defaultdict
n = int(input()); 
num = [*map(int, input().split())]
c = Counter(num)
ans = 0
for x in range(min(num), max(num)+1):
    ans = max(ans, c[x-1]+c[x]+c[x+1])
print(ans)


