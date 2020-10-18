#自分の回答
s = input()
ans = ""
for _ in range(len(s)):
    if s[0] == "0":
        ans += "0"
        s = s[1:]
    elif s[0] == "1":
        ans += "1"
        s = s[1:]
    else:
        s = s[1:]
        ans = ans[:-1]
print(ans)

#ほかの回答
s = input()
res = ""
for i in range(len(s)):
    if s[i] == "1" or s[i] == "0":
        res += s[i]
    elif s[i] == "B" and len(res) != 0:
        res = res[:-1]
 
print(res)

#joinを使う方法
s = input()
ans = []
for i in s:
    if i == "0" or i == "1":
        ans.append(i)
    elif i == "B" and len(ans) == 0:
        continue
    elif i == "B":
        print("B")
print("".join(ans))