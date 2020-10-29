class Dice:
    def __init__(self):
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]

    def setnum(self, n1, n2, n3, n4, n5, n6):
        self.number[0] = n1
        self.number[1] = n2
        self.number[2] = n3
        self.number[3] = n4
        self.number[4] = n5
        self.number[5] = n6
    
    def roll(self, dir):
        for i in range(6):
            self.work = self.number

        if dir == "N":
            self.setnum(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        if dir == "E":
            self.setnum(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        if dir == "S":
            self.setnum(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1])
        if dir == "W":
            self.setnum(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])

n = int(input())
dice = [Dice() for _ in range(n)]
for i in range(n):
    dice[i].setnum(*[*map(int, input().split())])
order = "NNNNWNNNWNNNENNNENNNWNNN"
for i in range(n):
    for j in range(i+1, n):
        for dir in order:
            dice[j].roll(dir)
            if dice[i].number == dice[j].number:
                print("No")
                exit()
                       
print("Yes")