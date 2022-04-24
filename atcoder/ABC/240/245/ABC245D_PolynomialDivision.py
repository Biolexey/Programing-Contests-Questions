#numpyライブラリの多項式モジュールを利用
from numpy import poly1d
 
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
 
polyA = poly1d(list(reversed(A)))
polyC = poly1d(list(reversed(C)))
 
# Bを求める
polyB = polyC / polyA


# Bの係数 ※print(polyB)=(poly1d([2., 4., 6.]), poly1d([0.]))と第二変数が剰余になるのでpoly[0]で商を指定
coefB = list(map(int, polyB[0].c))
 
# 順番を逆にして出力
ans = list(reversed(coefB))
print(*ans)

#ライブラリを使わない方法
N, M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
 
B = [0]*(M+1)
 
for i in range(M+1):
    x = 0
    for k in range(1, i+1):
        if 0 <= N-k:
            x += A[N-k] * B[M-(i-k)]
        else:
            break
    
    B[M-i] = (C[M+N-i]-x)//A[N]
    
print(*B)