#自分の回答(リストだと先頭から要素を取り出すのにO(n)かかってしまうのでdequeを使った)
from collections import deque

n, q = map(int, input().split())
d = deque([name, int(time)] for name, time in [input().split() for _ in range(n)])

total = 0
while d:
    name, time = d.popleft()
    if time <= q:
        total += time
        print(name, total)
    else:
        total += q
        d.append([name, time - q])
