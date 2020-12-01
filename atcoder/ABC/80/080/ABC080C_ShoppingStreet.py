n = int(input())
f = [int(input().replace(" ", ""), 2) for _ in range(n)]
p = [[*map(int, input().split())] for _ in range(n)]
print(max(sum([p[bin(f&i).count("1")] for f, p in zip(f, p)]) for i in range(1, 2**10)))
#test
