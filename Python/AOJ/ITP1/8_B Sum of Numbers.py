while 1:
    num = input()
    if num == "0":
        break
    li = list(num)
    ans= 0
    for i in li:
        ans += int(i)
    print(ans)

#別解1
while 1:
    num = input()
    if num[0] == "0":
        break
    print(sum(int(i) for i in num))

#別解2
while 1:
    s = input()
    if s == "0":
        break
    print(sum(list(map(int, s))))

#別解3
for x in iter(input, "0"):#input()の値が"0"になるまでイテレータを返し続ける("0"単体のみ)
    print(sum(map(int, x)))