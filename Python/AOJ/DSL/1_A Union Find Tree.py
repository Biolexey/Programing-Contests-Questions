class UnionFind:
    def __init__(self, n):
        self.n = n
        self.pa = [-1]*n #負の値なら自分が根でその絶対値がsize
    
    def root(self, a):
        if self.pa[a] < 0:#自分が根ならその番号を
            return a
        self.pa[a] = self.root(self.pa[a])#自分の親をすべて根の番号に変える
        return self.pa[a]#最終的に根の番号が返ってくる

    def size(self, a):
        return -self.pa[self.root(a)]#aの根の絶対値を返す

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False
        if self.size(a) < self.size(b):#サイズの小さいbをサイズの大きいaに結合したい
            a, b= b, a
        self.pa[a] += self.pa[b]
        self.pa[b] = a#bの親をaにすることでbの子はroot()ですべて根がaになる

    def same(self, a, b):
        return self.root(a) == self.root(b)

n, q = map(int, input().split())
u = UnionFind(n)
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        u.unite(x, y)
    else:
        print(1 if u.same(x, y) else 0)

#重み付きUnionFindTree
class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            px = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = px
            return px
 
    def union(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y, w = y, x, -w
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weight[y] = w
        return
 
    def diff(self, x, y):
        return self.weight[y] - self.weight[x]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}