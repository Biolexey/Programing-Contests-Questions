n, k = map(int, input().split())
L = sorted([*map(int, input().split())], reverse=1)
print(sum(L[:k]))
