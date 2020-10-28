n = int(input())
vec = [[*map(int, input().split())] for _ in range(2)]

def dest(p, vec, n):
    if p != float("inf"):
        return (sum(abs(vec[0][i]-vec[1][i])**p for i in range(n)))**(1/p)
    else:
        return max((abs(vec[0][i]-vec[1][i]) for i in range(n)))

for p in [1, 2, 3, float("inf")]:
    print(dest(p, vec, n))