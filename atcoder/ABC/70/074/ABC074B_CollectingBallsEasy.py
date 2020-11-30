n = int(input())
k = int(input())
X = [*map(int, input().split())]
print(2*sum(min(X[i], abs(k-X[i])) for i in range(n)))