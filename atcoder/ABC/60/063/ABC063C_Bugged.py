n = int(input())
num = [int(input()) for _ in range(n)]
not10 = sorted([x for x in num if x % 10 != 0])#10の倍数でない問題
print(sum(num) if sum(num)%10 != 0 else sum(num)-not10[0] if not10 else 0)



