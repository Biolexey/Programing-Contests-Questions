# #自分の回答(これではN=2*10^5に対してO(N^2)の計算量がかかってしまうため実行時間制限超過になってしまう)
# s = str(input())
# count = 0
# for i in range(0,len(s)+1):
#     for j in range(i+1,len(s)+1):
#         if int(s[i:j])%2019 == 0:
#             count += 1

# print(count)

#ほかの回答
s = input()[::-1] # 入力文字列を逆順でsに格納

counts = [0] * 2019
counts[0] = 1

num, d = 0, 1

for char in s:
    num += int(char) * d
    num %= 2019
    d *= 10
    d %= 2019
    counts[num] += 1

ans = 0
for cnt in counts:
    ans += (cnt * (cnt - 1)) // 2

print(ans) # 答えの出力
