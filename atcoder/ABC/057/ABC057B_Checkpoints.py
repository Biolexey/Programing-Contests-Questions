n, m = map(int, input().split())
stu = [[*map(int, input().split())] for _ in range(n)]
chk = [[*map(int, input().split())] for _ in range(m)]

def distance(a1, a2, b1, b2):
    return abs(a1-b1)+abs(a2-b2)

for i in range(n):
    dest = 1
    min = float("inf")
    for j in range(m):
        if distance(stu[i][0], stu[i][1], chk[j][0], chk[j][1]) < min:
            min = distance(stu[i][0], stu[i][1], chk[j][0], chk[j][1])
            dest = j+1
    print(dest)