import math

#脳死の方法
for i in range(2,100):
    if 0 not in [i % j for j in range(2, i//2 + 1)]:
#i//2にしないとfloat型になってしまう
        print(i)

#少しまともな方法
for i in range(2,100):
    if 0 not in [i % j for j in range(2, int(math.sqrt(i) + 1))]:
        print(i)

#さらに高速
a = [i for i in range(2, 101)]
for i in range(2, int(100**0.5)):
    a = [x for x in a if (x == i or x % i != 0)]
for j in a:
    print(j)

#エラトステネスの篩
a = [i for i in range(2, 101)]
prime = []
while a[0] <= math.sqrt(100):
    prime.append(a[0])
    tmp = a[0]
    a = [i for i in a if i % tmp != 0]
prime.extend(a)
for i in prime:
    print(i)

