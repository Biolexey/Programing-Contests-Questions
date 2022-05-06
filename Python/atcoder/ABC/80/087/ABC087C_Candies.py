n = int(input())
candy = [[*map(int, input().split())] for _ in range(2)]
ans = 0
for i in range(n):
    ans = max(ans, sum(candy[0][0:i+1])+sum(candy[1][i:n+1]))
print(ans)