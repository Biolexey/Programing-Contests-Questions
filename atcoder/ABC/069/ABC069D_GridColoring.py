h, w = map(int, input().split())
n = int(input())
A = [*map(int, input().split())]
ans = []
for i in range(n):
    ans += [i+1]*A[i]

for i in range(h):
    print(*sorted(ans[w*i:w*(i+1)], reverse=i%2))