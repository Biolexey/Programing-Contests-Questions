from collections import deque
import math

k = int(input())
dist = [math.inf]*k
dist[1] = 1
q = deque([1])

while q:
    v = q.popleft()
    if dist[v*10 % k] > dist[v]:
        dist[v*10 % k] = dist[v]
        q.appendleft(v*10 % k)
    
    if dist[(v+1) % k] > dist[v]:
        dist[(v+1) % k] = dist[v] + 1
        q.append((v+1) % k)

print(dist[0])