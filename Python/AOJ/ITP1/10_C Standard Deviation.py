while 1:
    n = int(input())
    if n == 0:
        break
    score = [*map(int, input().split())]
    ave = sum(score)/n
    var = sum((i-ave)**2 for i in score)/n
    stdev = (var)**0.5
    print(ave)

#もっと楽にすると
from statistics import pstdev, pvariance, mean
while 1:
    n = int(input())
    if n == 0:
        break
    score = [*map(int, input().split())]
    print(pstdev(score))