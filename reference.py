#数字かどうか判定
 #全ての文字が十進数字なら真、そうでなければ偽(半角・全角のアラビア数字が真)
str.isdecimal()
 #全ての文字が数字なら真、そうでなければ偽(半角・全角のアラビア数字、特殊数字が真)
str.isdigit()
 #全ての文字が数を表す文字なら真、そうでなければ偽(半角・全角のアラビア数字、特殊数字、漢数字が真)
str.isnumeric()
#英字かどうか判定
 #全ての文字が英字なら真、そうでなければ偽(便宜上「英字」と書いているが、平仮名やカタカナ、漢字なども真)
str.isalpha()
#英数字かどうか判定
 #全ての文字が英数字なら真、そうでなければ偽(各文字が上のメソッドで真となれば真)
str.isalnum()
#負の数や少数でもTrueにしたいなら,.-などをreplaceしたり、float()で変換可能か判定すればよい

from collections import Counter, deque
#counterはリストやイテレータからすべての値の出現回数をカウントする
#s.keys(), s.values(), s.items(), list(s)で要素を抽出できる
s = Counter("Qiita")
print(s)
print(s["i"])
#>Counter({'i': 2, 'Q': 1, 't': 1, 'a': 1})
#>2

#dequeはキューとして使用することが出来る
d = deque([[1, 2], 2, 3, 4])
print(d.pop())
print(d.popleft())
d.append(1)
d.appendleft(4)
print(d)
# >4
# >[1, 2]
# >deque([4, 2, 3, 1])

import itertools
d = [1,2,3,4,5]
#累積和
a = itertools.accumulate(d)
print(a)
# >1 3 6 10 15
#全探索
#順列
print(list(itertools.permutations([1, 2, 3])))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#組み合わせ
print(list(itertools.combinations([1, 2, 3], 2)))
# -> [(1, 2), (1, 3), (2, 3)]
#直積
print(list(itertools.product([0,1], repeat=3)))
# -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

#アルファベット小文字
[chr(i) for i in range(97, 97+26)]
[chr(i) for i in range(ord('a'), ord('z')+1)]
#アルファベット大文字
[chr(i) for i in range(65, 65+26)]
[chr(i) for i in range(ord('A'), ord('Z')+1)]
#半角数字
[chr(i) for i in range(48, 48+10)]
[chr(i) for i in range(ord('0'), ord('9')+1)]
#ひらがな
[chr(i) for i in range(12353, 12436)]
[chr(i) for i in range(ord('ぁ'), ord('ん')+1)]
#カタカナ
[chr(i) for i in range(12449, 12532+1)]
[chr(i) for i in range(ord('ァ'), ord('ン')+2)]
# 「ヴ」がいらない場合は「-1」してください
#全角数字
[chr(i) for i in range(65296, 65296+10)]
[chr(i) for i in range(ord('０'), ord('９')+1)]