N = int(input())
S = list(input())
S += S[0]

for f, s in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    x = [f, s]
    for i in range(1, N+1):
        if S[i] == "o":
            f, s = s, (f ^ s)
        else:
            f, s = s, not(f ^ s)
        x.append(s)
    if x[0] == x[N] and x[1] == x[N+1]:
        x.pop()
        x.pop()
        print("".join(["W" if x else "S" for x in x]))
        exit()
print("-1")
