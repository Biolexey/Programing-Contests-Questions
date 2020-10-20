from heapq import heapify, heappop

n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
heap = [[float("inf"), v] for v in range(n)]#現在いる頂点からほかの各頂点までのコストを格納する
heap[0] = [0, 0]#0を始点とする
weight = 0
while heap:
    heapify(heap)#heapを再更新
    w, u = heappop(heap)
    weight += w#u=0のときはw=0
    for i, [w, v] in enumerate(heap):#今いる点(u)からの各頂点へのコストを更新
        if 0<= s[u][v] < w:
            heap[i] = [s[u][v], v]
print(weight)

#scipyを使えばscipy.sparce.csgraph.minimum_spanning_tree()で求まる(引数は２次リストやNumpy配列)
