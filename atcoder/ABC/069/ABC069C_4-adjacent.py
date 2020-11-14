n = int(input())
A = [*map(int, input().split())]
cnt1, cnt2, cnt4 = 0, 0, 0
for a in A:
    if a % 2 == 0:
        if a % 4 == 0:
            cnt4 += 1
            continue
        cnt2 += 1
    else:
        cnt1 += 1

judge = False
if cnt2:
    if cnt1 <= cnt4:
        judge = True
else:
    if cnt1 <= cnt4 + 1:
        judge = True

print("Yes" if judge else "No")
