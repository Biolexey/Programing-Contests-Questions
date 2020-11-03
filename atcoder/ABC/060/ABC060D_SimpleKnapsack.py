#典型的な2次元DPを用いたのだがテストケース何個かで実行時エラー(理由がわからない)
n, w = map(int, input().split())
item = [[*map(int, input().split())] for _ in range(n)]
dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        if item[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i-1][0]]+item[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][w])

#ひとつ前のDPを保存する(実質)1次元DPでやったら通った
N, W = map(int, input().split())
Items = [[*map(int, input().split())] for _ in range(N)]
from collections import defaultdict as dd
Bag = dd(lambda:0)#初期化 
Bag[0] = 0
for w,v in Items:
    temp = [(key+w,Bag[key]+v) for key in Bag if key + w <= W]#新しい値を保持しておく
    for key,value in temp:
        Bag[key] = max(Bag[key],value)#今の値と比較して大きければ交換
ans = max(Bag.values())
print(ans)

