class Node:
  def __init__(self, chs, pa=-1):
    self.chs = chs
    self.pa = pa

n = int(input())
tree = {id:Node(chs=[-1,-1]) for id in range(-1, n)}
for _ in range(n):
  id, *chs = map(int, input().split())
  tree[id].chs = chs
  for ch in chs:
    tree[ch].pa = id

def walk(id, order):
  walked = ""
  if id != -1:
    if order == "Pre":
      walked += f" {id}"
    walked += walk(tree[id].chs[0], order)
    if order == "In":
      walked += f" {id}"
    walked += walk(tree[id].chs[1], order)
    if order == "Post":
      walked += f" {id}"
  return walked

for id in tree:
  if tree[id].pa == -1:
    for order in ["Pre", "In", "Post"]:
      print(order + "order\n" + walk(id, order))      
    break