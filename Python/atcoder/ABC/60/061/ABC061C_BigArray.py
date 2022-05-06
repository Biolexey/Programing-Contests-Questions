#おそらくTLEになるだろうなと思いながら書いた(もちろんTLEになったw)
n, k = map(int, input().split())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    for _ in range(b):
        li.append(a)
li.sort()
print(li[k-1])

#それぞれの数字の個数をdict形式で保存しておき、kに応じて出力する方法にした
n, k = map(int, input().split())
nums = dict()
for _ in range(n):
    a, b = map(int, input().split())
    if a in nums:
        nums[a] += b
    else:
        nums[a] = b
ans = sorted(nums.items(), key = lambda x: x[0])#dictをkeyでソート(.sort()は使えない)
sum = 0
for i in range(len(ans)):
    sum += ans[i][1]
    if k <= sum:
        print(ans[i][0])
        exit()

#各数字をインデックス荷物リストを作っといてそこに個数を保管しておく方法もある
n, k = map(int, input().split())
nums = [0]*(10**5+1)
for _ in range(n):
    a, b = map(int, input().split())
    nums[a] += b
sum = 0
for i in range(10**5+1):
    if nums[i]:
        sum += nums[i]
    if sum >= k:
        print(i)
        exit()
