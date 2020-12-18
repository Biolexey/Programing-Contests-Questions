n = int(input())
kinds = []
num = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(n):
    s = input()
    if s[0] in num:
        if s[0] not in kinds:
            kinds.append(s[0])
        num[s[0]] += 1
ans = 0
for i in range(0, len(kinds)-2):
    for j in range(i+1, len(kinds)-1):
        for k in range(j+1, len(kinds)):
            ans += num[kinds[i]]*num[kinds[j]]*num[kinds[k]]
print(ans)
    