n = int(input())
path = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)

def dfs(x):
    visit = [-1]*n
    visit[x] = 0
    temp = [x]
    while temp:
        p = temp.pop()
        for i in path[p]:
            if visit[i] != -1:
                continue
            visit[i] = visit[p]+1
            temp.append(i)
    return visit

l1 = dfs(0)
l2 = dfs(n-1)
cnt = 0
for i in range(n):
    if l1[i] <= l2[i]:
        cnt += 1

print("Fennec" if cnt > n - cnt else "Snuke")