def func(a, b):#関数を定義
    return min(len(str(a)), len(str(b)))

c = func(1,10000)
print(c)