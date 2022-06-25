n = int(input())
s = input()
W = list(map(int, input().split()))

S = 0
X = 0
for i in range(n):
    print(S)
    if s[i] == "1":
        S += W[i]
        X -= 1
    else:
        S -= W[i]
        X += 1
print(S, X)