#自分の回答
N = int(input())
a = []
for i in range(N):
    a.append(input())
print(len(set(a)))

#簡潔
N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))
