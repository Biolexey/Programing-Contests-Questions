class Node:
    def __init__(self, pa = -1, chs = None):
        self.pa = pa
        self.chs = chs

n = int(input())
tree = {id: Node() for id in range(n)}
for _ in range(n):
    id, _, *chs = map(int, input().split())
    tree[id].chs = chs
    for ch in chs:
        tree[ch].pa = id

def depths(id, depth):
    tree[id].depth = depth
    for ch in tree[id].chs:
        depths(ch, depth+1)

for id in tree:
    if tree[id].pa == -1:
        depths(id, 0)
        break

for id, node in tree.items():
    kind = "root" if node.pa == -1 else "internal node" if node.chs else "leaf"
    print(f"node {id}: parent = {node.pa}, depth = {node.depth}, {kind}, {node.chs}")