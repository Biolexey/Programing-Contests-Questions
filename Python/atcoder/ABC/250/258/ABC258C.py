import sys

input = sys.stdin.readline
n, q = map(int, input().split())
s = list(input())
s = s[:-1]

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        tmp = s[-x:]
        s = s[:-x]
        s = tmp+s
    else:
        print(s[x-1])