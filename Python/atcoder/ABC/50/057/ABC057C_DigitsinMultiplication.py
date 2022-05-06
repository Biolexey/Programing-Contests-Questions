from collections import deque
n = int(input())

def func(a, b):#関数を定義
    return max(len(str(a)), len(str(b)))

#nに対する約数を求める
li = []
for i in range(n%2, int(n**0.5)+1, n%2+1):
    if i != 0:
        if n%i == 0:
            li.append(int(i))
            li.append(int(n/(i)))
li.sort()
que = deque(li)
ans = float("inf")

while que:
    a, b = int(que.popleft()), int(que.pop())
    c = func(a, b)
    if ans > c:
        ans = c

print(ans)

#もっと簡単にするなら
n = int(input())

i = int(n**0.5)
while n%i != 0:
    i -= 1
print(len(str(n//i)))
