from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]
num_w = sum(s[i].count(".") for i in range(w))

dir = ([1,0], [0,1], [-1,0], [0,-1])
que = deque([(0,0,0)])
used = {(0, 0)}

res = None
while que:
    p, q, cost = que.popleft()
    if p == w-1 and q == h-1:
        res = cost
        break
    for d1, d2 in dir:
        dp = p + d1
        dq = q + d2
        #print(f"{p},{q}で{dp},{dq}に進もうとしています")
        if (not 0 <= dp < w) or (not 0 <= dq < h) or s[dq][dp] == "#" or (dp, dq) in used:
            #print("無理でした")
            continue
        #print("いけました")
        used.add((dp, dq))
        que.append((dp, dq, cost+1))
        #print(used, que)

if res:
    print(num_w - 1 - res)
else:
    print(-1)