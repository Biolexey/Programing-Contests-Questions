n = int(input())
A = [*map(int, input().split())]
S = sum(A)
sumup = 0
ans = 10**15
for i in range(n-1):
    sumup += A[i]
    if abs(S-2*sumup) < ans:
        ans = abs(S-2*sumup)
print(ans)