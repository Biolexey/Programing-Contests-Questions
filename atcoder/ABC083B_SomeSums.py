#自分の回答
N, A, B = map(int, input().split())
result = 0
for i in range(N+1):
    if A <= sum(map(int, str(i))) <= B:
        result += i
print(result)

#簡潔
N, A, B = map(int, input().split())
print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))