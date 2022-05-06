N = int(input())
names = []
for _ in range(N):
    s, t = input().split()
    names.append(s)
    names.append(t)

print("No" if len(set(names)) <= (N-1)*2 else "Yes")