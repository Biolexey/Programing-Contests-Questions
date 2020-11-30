n = int(input())
cor = [[*map(int, input().split() + [i])] for i in range(n)]
xsort = sorted(cor, key=lambda x: x[0])
ysort = sorted(cor, key=lambda x: x[1])

dis = []
for [x0, _, i0], [x1, _, i1] in zip(xsort, xsort[1:]):
    dis.append([(x1-x0), i0, i1])
for [_, y0, i0], [_, y1, i1] in zip(ysort, ysort[1:]):
    dis.append([(y1-y0), i0, i1])
dis.sort(key=lambda x: x[0])


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
        self.pa[b] = a #bの親をaにすることでbの子はroot()ですべて根がaになる

    def same(self, a, b):
        return self.root(a) == self.root(b)

uf = UnionFind(n)
ans= 0
for d, a, b in dis:
    if uf.same(a, b):
        continue
    uf.unite(a, b)
    ans += d
print(ans)
