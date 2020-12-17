C = [[*map(int, input().split())] for _ in range(3)]
b1 = C[0][0]
b2, b3, a2, a3 = C[0][1], C[0][2], C[1][0]-b1, C[2][0]-b1
print("Yes" if C[1][1] == a2+b2 and C[1][2] == a2+b3 and C[2][1] == a3+b2 and C[2][2] == a3+b3 else "No")