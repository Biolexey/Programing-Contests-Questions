N, K = map(int, input().split())
AB = list(list(map(int, input().split())) for _ in range(2))

#dpで解く
dp = list([0]*N for _ in range(2))
dp[0][0], dp[1][0] = 1, 1

for j in range(1, N):
    for i in range(2):      #比較元をここで指定
        for k in range(2):  #一個前の列を走査
            if abs(AB[i][j]-AB[k][j-1]) <= K and dp[k][j-1]:#比較対象のdpが1かつ条件を満たす場合
                dp[i][j] = 1#dpを１に更新

for i in range(2):
    if dp[i][N-1] == 1:
        print("Yes")
        exit()
print("No")