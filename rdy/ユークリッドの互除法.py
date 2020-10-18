a, b = map(int,input().split())

#再起関数
def euc(a, b):
    if b > a :
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return euc(b, a % b)

print("最小公約数は" + str(euc(a, b)) + "です")

#最小公倍数
print("最小公倍数は" + str(int((a * b) / euc(a, b))) + "です")

