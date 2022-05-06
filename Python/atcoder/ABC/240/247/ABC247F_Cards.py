class dsu():
    n = 1
    parent_or_size = [-1 for i in range(n)]
 
    def __init__(self, N):
        self.n = N
        self.parent_or_size = [-1 for i in range(N)]
 
    def merge(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if (-self.parent_or_size[x] < -self.parent_or_size[y]):
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x
 
    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)
 
    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if (self.parent_or_size[a] < 0):
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]
 
    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]
 
    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2
 
 
N = int(input())
P = [int(x)-1 for x in input().split()]
Q = [int(x)-1 for x in input().split()]
 
UF = dsu(N)
for p, q in zip(P, Q):
    UF.merge(p, q)
 
L = [0] * (N + 1)
L[0] = 2
L[1] = 1
mod = 998244353
 
for i in range(2, N + 1):
    L[i] = L[i - 1] + L[i - 2]
    L[i] %= mod
ans =1
for r in UF.parent_or_size:
    if r >= 0:
        continue
    s = -r
    ans *= L[s]
    ans %= mod
print(ans)