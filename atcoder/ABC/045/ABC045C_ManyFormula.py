s = str(input())
ans = 0
for i in range(2**(len(s) - 1)):
    l = s[0]
    for j in range(len(s)-1):
        if (i >> j) & 1:
            l += "+"
        l += s[j+1]
    ans += eval(l)#eval関数は文字列を数式としてその解を返す
print(ans)