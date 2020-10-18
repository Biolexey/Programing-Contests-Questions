#自分の回答
count = int(input())
num = list(map(int, input().split()))
a = 0
while all(i % 2 == 0 for i in num):
    for j in range(count):
        num[j] /= 2
    a += 1
print(a)

#簡潔
N = int(input())
A = list(map(int, input().split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)