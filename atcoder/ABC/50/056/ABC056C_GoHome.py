x = int(input())
t, l = 0, 0
while l < x:#1+2+....+kで総和がxを超えているときその部分和でxにすることが出来る
    t += 1
    l += t
print(t)