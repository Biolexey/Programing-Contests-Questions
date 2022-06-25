import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
path = [[] for _ in range(n)]       # 部屋からの移動可能経路
for i in range(n-1):                # i:0 -> n-2
    idx = i+1                       # idx: 1 -> n-1
    a, b = p[i]-1, idx              # 互いに繋がっている部屋
    path[a].append(b)               # 追加
    path[b].append(a)

def bfs(n, start, path):            # 幅優先探索
    cnt = 1                         # 距離が3以下の部屋の数
    distance = [-1]*n               # スタート地点からの距離(未探索は-1)
    distance[start] = 0             # スタート地点の距離を0に初期化
    q = deque()                     # q : 待機キュー
    q.append(start)
    while len(q)>0:                                        
        now = q.popleft()           # 現在地
        for go in path[now]:        # 行き先選択                  
            if distance[go] == -1 and distance[now] < 3: # 行き先が未探索かつ現在の移動距離が3未満
                q.append(go)
                distance[go] = distance[now]+1 # 移動コストを自分+1
                cnt += 1            # 条件を満たす部屋の数を+1
    return cnt


if __name__ == '__main__':
    ans = []
    for i in range(n):
        ans.append(bfs(n, i, path))
    print(*ans)
    