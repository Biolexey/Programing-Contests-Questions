n, k= map(int, input().split())
cards = [*map(int, input().split())]
cards.sort(reverse = True)
ans = n
s, cnt = 0, 0
for i in cards:
    cnt += 1
    if s+i < k:
        s += i
    else:
        ans = n - cnt
print(ans)