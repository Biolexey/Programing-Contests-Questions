x = int(input())
ans = 2*(x//11)
if x % 11 == 0:
    print(ans)
elif x % 11 < 7:
    print(ans + 1)
else:
    print(ans + 2)

