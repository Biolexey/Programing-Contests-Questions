# l = [0]*4
# for i in range(4):
#     li = l[:]
#     for j in range(3):
#         l[j+1] = li[j] + 1
#     print(l)

a = [1,2,3]
b = a
b[0] = 5
print(a,b)