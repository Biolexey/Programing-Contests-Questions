class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n #負の値ならその絶対値がサイズ
        self.weight = [0] * n
 
    def find(self, x):
        if self.parents[x] < 0:#自分が根ならその番号を返す
            return x
        else:
            px = self.find(self.parents[x])#再帰的に根を求める
            self.weight[x] += self.weight[self.parents[x]]#根からの重さを再計算
            self.parents[x] = px#自分の親の番号を根に変える
            return px#最終的に根の番号を返す
 
    def union(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y, w = y, x, -w
        self.parents[x] += self.parents[y]#よりサイズが小さい(根として大きい)方に連結
        self.parents[y] = x#連結したほうの親に連結された方の番号を登録
        self.weight[y] = w#重さを登録
        return
 
    def diff(self, x, y):#xとyの重さの差を返す
        return self.weight[y] - self.weight[x]
 
    def same(self, x, y):#xとyの根が同じかどうかを返す
        return self.find(x) == self.find(y)
 
    def size(self, x):#その番号が属する木のサイズを返す
        return -self.parents[self.find(x)]
 
    def members(self, x):#xと同じ木に属する番号を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):#根になっている番号とそのサイズを返す
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):#いくつ木があるかを返す
        return len(self.roots())
 
    def all_group_members(self):#各木の根と属する番号を全表示
        return {r: self.members(r) for r in self.roots()}

n, m = map(int, input().split())
uf = WeightedUnionFind(n)
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if uf.same(l, r):
        if uf.diff(l, r) != d:
            print("No")
            exit()
    else:
        uf.union(l, r, d)
    print(uf.parents)
    print(uf.weight)
print("Yes")