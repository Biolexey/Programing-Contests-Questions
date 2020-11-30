#自分の回答
a, b, c = map(int, (input().split()))
print(len(set([a, b, c])))

#別解
l = list(map(int, input().split()))
print(len(set(l)))
