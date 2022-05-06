#特定の連続した数を表す->referenceを参照してください
import sys
s = sys.stdin.read().lower()
for x in map(chr, range(97, 123)):
    print(x, ":", s.count(x))

#別解1
dic = {chr(i):0 for i in range(97, 97+26)}
while 1:
    try:
        s = input().lower()
        for i in s:
            if i in dic:
                dic[i] += 1
    except:
        break
for x, y in dic.items():
    print(x,":",y)
