n = int(input())
s = [*map(int, input().split())]

for i in range(n):
    print(f"node {i+1}: key = {s[i]}, ", end = "")
    print(f"parent key = {s[(i-1)//2]}, " if i else "", end = "")
    print(f"left key = {s[2*i+1]}, " if 2*i+1<n else "", end = "")
    print(f"right key = {s[2*i+2]}, " if 2*i+2<n else "")