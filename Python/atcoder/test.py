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

print(make_divisors(int(input())))