from functools import reduce

#for分を使った
s = 0
for i in range(1,51):
    s += i
print(s)

#sum関数を使った
print(sum(range(1,51)))

#generator式を使った
print(sum(x for x in range(1,51)))

#reduceを使った
print(reduce(lambda x, y:x + y, range(1,51)))
