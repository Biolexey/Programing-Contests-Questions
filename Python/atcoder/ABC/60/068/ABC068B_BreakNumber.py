n = int(input())
num = [64, 32, 16, 8, 4, 2, 1]
for i in num:
    if n >= i:
        print(i)
        exit()