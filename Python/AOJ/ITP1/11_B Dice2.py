class Dice:
    def __init__(self):
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]
        self.order = "NNNNWNNNWNNNENNNENNNWNNN"

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

    def query(self, top, front):
        self.savedata = [i for i in range(6)]
        for i in range(6):
            self.savedata[i] = self.number[i]
        
        ans = -1

        for dir in self.order:
            self.roll(dir)
            if self.number[0] == top and self.number[1] == front:
                ans = self.number[2]
                break
        
        for i in range(6):
            self.number[i] = self.savedata[i]
        
        return ans

dice = Dice()
num = [*map(int, input().split())]
dice.setnum(*num)
n = int(input())
for i in range(n):
    print(dice.query(*map(int, input().split())))