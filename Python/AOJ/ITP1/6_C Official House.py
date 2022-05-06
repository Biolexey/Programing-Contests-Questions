rooms = [[[0]*10 for _ in range(3)] for _ in range(4)]
n = int(input())
for i in range(n):
    house, floor, room, ppl = map(int, input().split())
    rooms[house-1][floor-1][room-1] += ppl

x = 0
for i in range(4):
    if x != 0:
        print("#"*20)
    x = 1

    for floors in rooms[i]:
        print("", *floors, end = "")
        print()