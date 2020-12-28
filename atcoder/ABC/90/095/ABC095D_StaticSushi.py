from itertools import accumulate
n, c = map(int, input().split())
x, v, xrev, vrev = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    X, V = map(int, input().split())
    x[i], v[i] = X, V
    xrev[n+1-i] = c-X
    vrev[n+1-i] = V

vacc = list(accumulate(v))
vrevacc = list(accumulate(vrev))

A, B, C, D = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    A[i] = max(A[i-1], vacc[i]-x[i])
    B[i] = max(B[i-1], vacc[i]-x[i]*2)
    C[i] = max(C[i-1], vrevacc[i]-xrev[i])
    D[i] = max(D[i-1], vrevacc[i]-xrev[i]*2)

ans = 0
for i in range(n+1):
    tmp1 = A[i]+D[n-i]
    tmp2 = B[i]+C[n-i]
    ans = max(ans, tmp1, tmp2)
print(ans)
