#自分の回答
N, L = map(int,input().split())
l = [input() for _ in range(N)]
l1 = sorted(l)
print(*l1, sep ="")

#簡潔
n, l = map(int, input().split())
l = [input() for _ in range(n)]
l.sort()
print("".join(l))

#または
n, l = map(int, input().split())
print("".join(sorted(input() for _ in range(n))))