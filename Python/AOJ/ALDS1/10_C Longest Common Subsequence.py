# #トップダウン(TLE)
# for _ in range(int(input())):
#     x, y = input(), input()

#     def lcs(i,j):
#         if i == 0 or j == 0:
#             return 0
#         if x[i-1] == y[j-1]:
#             return lcs(i-1,j-1)+1
#         return max(lcs(i-1,j), lcs(i,j-1))

#     print(lcs(len(x), len(y)))

# #ボトムアップ(TLE)
# for _ in range(int(input())):
#     x, y = input(), input()
#     dp = [[0]*(len(y)+1) for _ in range(len(x)+1)]
#     for i in range(len(x)):
#         for j in range(len(y)):
#             dp[i+1][j+1] = dp[i][j]+1 if x[i] == y[j] else max(dp[i][j+1], dp[i+1][j])
#     print(dp[-1][-1])

#ボトムアップvol2
def lcs(X, Y):
    l = [0] * (len(Y)+1)
    for x in X:
        pre_l = l
        for j, y in enumerate(Y):
            if x == y:
                print(pre_l[j])
                l[j+1] = pre_l[j]+1
            elif l[j+1] < l[j]:
                l[j+1] = l[j]
        print(l)
    return l[-1]

for _ in range(int(input())):
    print(lcs(input(), input()))