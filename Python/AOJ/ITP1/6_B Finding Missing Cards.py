cards = [[0]*13 for _ in range(4)]#indexは0=S,1=H,2=C,3=D
marks = ["S", "H", "C", "D"]
n = int(input())
for _ in range(n):
    ma, num = input().split()
    cards[marks.index(ma)][int(num)-1] = 1

for i in range(4):
    for j in range(13):
        if cards[i][j] == 0:
            print(f"{marks[i]} {j+1}")
