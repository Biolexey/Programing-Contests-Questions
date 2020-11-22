#DPで解く
a, b, c, d, e, f = map(int, input().split())
a *= 100
b *= 100

dp = [-1 for _ in range(f+1)]

for i in range(a, f+1):
    if i % a == 0:
        dp[i] = 0
for i in range(a, f+1):
    if dp[i] != -1 and i + b <= f:
        dp[i+b] == 0
    if i % b == 0:
        dp[i] = 0

for i in range(a, f+1):
    if dp[i] == -1:
        continue
    if i+c <= f:
        if 100*(dp[i]+c) <= (i-dp[i])*e:
            dp[i+c] = max(dp[i+c], dp[i]+c) 
    if i+d <= f:
        if 100*(dp[i]+d) <= (i-dp[i])*e:
            dp[i+d] = max(dp[i+d], dp[i]+d)

for i in range(a, f+1):
    if dp[i] != -1:
        dp[i] = dp[i]*100/i
m = max(dp)
ind = dp.index(m)
print(ind, int(ind*m//100))

#普通に解く
a, b, c, d, e, f = map(int, input().split())
ans = [0]*2#[water,suger]
ma = 0#最大の濃度を保持
for i in range(f//100+1):#waterの量を全探索
    if i%a == 0 or i%b == 0:
        w = i*100
        limit = min(f-w, i*e)#sugerの量の上限
        s = 0
        for j in range(limit//c+1):#sugerの量を全探索
            cs = j*c#c[g]のsugerを使ったsugerの量
            s = max(s, cs+((limit-cs)//d)*d)#全sugerの量
        if w != 0:
            if ma <= (100*s)/(w+s):
                ans = [w, s]
                ma = (100*s)/(w+s)
print(ans[0]+ans[1], ans[1])