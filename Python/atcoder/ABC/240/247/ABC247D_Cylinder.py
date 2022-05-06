from collections import deque

Q = int(input())
deq = deque()
for _ in range(Q):
    num, *i = map(int, input().split())
    if num == 1:
        x, c = i
        deq.append([x, c])
    else:
        c = i[0]
        ans = 0
        while c > 0:
            num, cnt = deq[0]
            if c >= cnt:
                ans += cnt*num
                deq.popleft()
                c -= cnt
            else:
                ans += c*num
                deq[0][1] -= c
                c = 0
        print(ans)