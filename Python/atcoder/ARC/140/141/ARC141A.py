t = int(input())

def make_divisors(n):                           # 約数関数
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    upper_divisors.reverse()
    return lower_divisors + [i for i in upper_divisors if i <= n//2]


for _ in range(t):
    num = input()
    div = make_divisors(len(num))               # 約数列挙
    ans = 11
    #print(div)

    for i in div:
        count = len(num)//i
        block = num[:i]
        tmp = int(block*count)
        if tmp <= int(num) and ans < tmp:
            ans = tmp

        block2 = str(int(block)-1)
        tmp1 = int(block2*count)
        if tmp1 <= int(num) and ans < tmp1:
            ans = tmp1

        tmp3 = int("9"*(len(num)-1))
        if tmp3 <= int(num) and ans < tmp3:
            ans = tmp3

    print(ans)
