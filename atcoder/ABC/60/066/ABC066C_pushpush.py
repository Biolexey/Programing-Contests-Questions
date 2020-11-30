from collections import deque
n = int(input())
num = [*map(int, input().split())]
ans = deque([])
for i in range(n):
    if i%2 != n%2:
        ans.appendleft(num[i])
    else:
        ans.append(num[i])
print(*ans)


