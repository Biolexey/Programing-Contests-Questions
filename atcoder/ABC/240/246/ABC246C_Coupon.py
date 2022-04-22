N, K, X = map(int, input().split())
A = list(map(int, input().split()))

#クーポン全額分使えるだけ使う
sumA = sum(A)
Q = sum([i // X for i in A])
sumA -= X * min(Q, K)

#使えるだけ使って余った端数を降順で格納
R = sorted([i % X for i in A], reverse=True)
K -= min(Q, K)
sumA -= sum(R[:K])
print(sumA)