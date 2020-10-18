def func(n):
    if n < 1:
        return 1
    else:
        return (161 * func(n-1) + 2457)%2**24

def func1(n):
    max = 1000000 + 1
    memo = [0 for _ in range(max)]
    memo[0] = 1
    for i in range(1, max):
        memo[i] = (161*memo[i-1]+2457) % 2**24
    return memo[n]

def func2(n):
    max = 1000000 + 1
    memo = [0 for _ in range(max)]
    memo[0] = 1
    for i in range(1, max):
        memo[i] = (1103515245*memo[i-1]+12345) % 2**26
    return memo[n]

def func3(n):
    max = 1000000 + 1
    memo = [0 for _ in range(max)]
    memo[0] = 1
    for i in range(1, max):
        memo[i] = (1103515245*memo[i-1]+12345) % 2**26
    for k in range(1, 1000000):
        for n in range(1000000 - k):
            if memo[n] == memo[n+k]:
                print(k)
                exit()


def solve2():
    cnt = 0
    for i in range(1,101):
        if func(i) % 2 == 0:
            cnt += 1
        else:
            None
    print(cnt)

def solve3():
    cnt = 0
    for i in range(1, 101, 2):
        if func(i) % 2 == 0:
            cnt += 1
        else:
            None
    print(cnt)

def solve4():
    print(func1(1000000))

def solve5():
    print(func2(2))
    print(func2(3))

def solve6():
    k = 1
    for i in range(1000000):
        if func2(i) == func2(i+k):
            print(k)
            exit()

print(func3(1000000))