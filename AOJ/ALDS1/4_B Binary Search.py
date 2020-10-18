n, s = int(input()), [*map(int, input().split())]
q, t = int(input()), [*map(int, input().split())]
cnt = 0
def binary_search(s,x):
    first, last = 0, len(s)
    while first < last:
        mid = (first+last)//2
        if x == s[mid]:
            return True
        if x < s[mid]:
            last = mid
        else:
            first = mid +1
    return False

print(sum(binary_search(s,x) for x in t))

#ほかの回答
import bisect
n, s = int(input()), [*map(int, input().split())]
q, t = int(input()), [*map(int, input().split())]

def binary_search(s, x):
    return x == s[bisect.bisect_left(s,x)]

print(sum(binary_search(s,x) for x in t))