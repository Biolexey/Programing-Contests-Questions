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

