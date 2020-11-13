k = int(input())
n = 50
div, mod = divmod(k, n)
num = [div + i for i in range(51)]
num.remove(div + n - mod)
print(50)
print(*num)

