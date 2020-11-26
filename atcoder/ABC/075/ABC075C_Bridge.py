#dfs
n, m = map(int, input().split())
path = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a] += [b]
    path[b] += [a]
v = list(range(1, n+1))

def dfs(v, path):
    for x in v:
        if len(path[x]) == 1:
            t = path[x][0]
            path[x] = []
            path[t].remove(x)
            v.remove(x)
            return dfs(v, path)+1
    return 0

print(dfs(v, path))

#unionfind
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
 
n, m = map(int, input().split())
 
ab = [list(map(int, input().split())) for i in range(m)]
 
ans = 0
for i in range(m):
    uf = UnionFind(n)
 
    for j in range(m):#j番目の道を使わずに木を生成
        if i == j:
            continue
 
        if uf.same(ab[j][0]-1, ab[j][1]-1):
            pass
        else:
            uf.unite(ab[j][0]-1, ab[j][1]-1)
 
    root = set()
    for k in range(n):
        root.add(uf.root(k))
 
    if len(root) != 1:
        ans += 1
 
print(ans)
