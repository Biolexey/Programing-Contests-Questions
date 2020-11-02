n = int(input())
li = [0]*n
for i in range(n):
    li[i] = input()

ans = ""

for k in [chr(i) for i in range(97, 97+26)]:
    sum = 50
    for j in range(n):
        sum = min(li[j].count(k), sum)
    ans += f"{k}"*sum

print(ans)

#open()を使って高速に行う(入力終了はCtrl+Z)
_,*s=open(0)
for c in sorted(set(s[0])):
    print(c*min(t.count(c)for t in s),end='')
print(s)

#Counterを使う
from collections import Counter
n = int(input())
s = Counter(input())

for _ in range(n-1):
    s &= Counter(input())

print("".join(sorted(s.elements())))