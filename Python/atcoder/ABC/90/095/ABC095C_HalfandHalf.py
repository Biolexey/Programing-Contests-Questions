a, b, c, x, y = map(int, input().split())
ans = 0
if a+b > 2*c:
    if x < y:
        large = "b"
    elif x > y:
        large = "a"
    else:
        large = "="
    ans += min(x, y)*2*c
    remain = max(x, y)-min(x, y)
    if large == "a":
        if a >= 2*c:
            ans += 2*c*remain
        else:
            ans += a*remain
    else:
        if b >= 2*c:
            ans += 2*c*remain
        else:
            ans += b*remain
    print(ans)
else:
    print(x*a+y*b)
