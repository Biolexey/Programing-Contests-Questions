n = int(input())
l = [*map(int, input().split())]
ans = 10**9
for i in range(n):
    x = l[i]
    cnt = 0
    while x%2 == 0:
        x /= 2
        cnt += 1
    ans = min(ans, cnt)
print(ans)

#別解
N = int(input())
A = list(map(int, input().split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)