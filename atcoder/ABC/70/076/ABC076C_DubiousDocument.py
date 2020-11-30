s, t = input(), input()
A = []
for i in range(len(s)-len(t)+1):
    cnt = 0
    for j in range(0, len(t)):
        if s[i+j] == t[j] or s[i+j] == "?":
            cnt += 1
            if cnt == len(t):
                ans = s[:i]+t+s[i+j+1:]
                ans = ans.replace("?", "a")
                A.append(ans)
        else:
            break
if A:
    print(min(A))
else:
    print("UNRESTORABLE")