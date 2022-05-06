#自分の回答(TLE多発)
n = int(input())
l = [input().split() for _ in range(n)]
ans = [0,0]
for i in range(n):
    ref_1 = int(l[i][0])
    ref_2 = int(l[i][1])
    for j in range(2,10**18-1):
        if (ans[0]>ref_1) or (ans[1]>ref_2):
            ref_1 = int(l[i][0])
            ref_2 = int(l[i][1])
            ref_1 *= j
            ref_2 *= j
        else:
            break

    ans[0], ans[1] = ref_1, ref_2
print(sum(ans))

#改善後(なぜかWAが出てくる)
import math
n = int(input())
l = [input().split() for _ in range(n)]
ans = [1,1]
for i in range(n):
    ref_1 = int(l[i][0])
    ref_2 = int(l[i][1])
    a = max(math.ceil(ans[0]/ref_1),math.ceil(ans[1]/ref_2))
    ans[0], ans[1] = a*ref_1, a*ref_2
print(ans[0] + ans[1])

#再構築(天井関数を使わずにやった)
n = int(input())
A, B = 0, 0
for i in range(n):
    x, y = map(int,input().split())
    dx, dy = 1, 1
    if A > x:
        dx = A // x
        if A % x != 0:
            dx += 1
    
    if B > y:
        dy = B // y
        if B % y != 0:
            dy += 1

    a = max(dx, dy)
    A, B = a * x, a * y
print(A + B)