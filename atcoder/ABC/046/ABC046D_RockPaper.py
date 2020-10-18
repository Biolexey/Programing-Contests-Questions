#自分の回答
s = input()
n = len(s)
gcount = 0
pcount = 0
score = 0
for i in range(n):
    if s[i] == "g":
        if gcount > pcount:
            pcount += 1
            score += 1
        else:
            gcount += 1
    else:
        if gcount > pcount:
            pcount += 1
        else:
            gcount += 1
            score -= 1
print(score)

#解説の簡潔な回答(自分のパーの数-相手のパーの数が答え)
import math
s = input()
n = len(s)
print(math.floor(n/2) - s.count("p"))
