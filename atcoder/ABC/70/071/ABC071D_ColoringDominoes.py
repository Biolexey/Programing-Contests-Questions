n = int(input())
s1 = input()+"0"
_ = input()+"0"
mod = 10**9+7
if s1[0] == s1[1]:
    ans = 6
    i = 2
    bef = 1
else:
    ans = 3
    i = 1
    bef = 0
while i < len(s1)-1:
    if s1[i] == s1[i+1]:
        if bef == 0:
            ans *= 2
        else:
            ans *= 3
        ans %= mod
        bef = 1
        i += 2
    else:
        if bef == 0:
            ans *= 2
        else:
            None
        ans %= mod
        bef = 0
        i += 1
print(ans%mod)
