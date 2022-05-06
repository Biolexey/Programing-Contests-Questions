s = input()
n = int(input())
for _ in range(n):
    cmd = input().split()
    op, x, y = cmd[0], cmd[1], cmd[2]
    if op == "print":
        print(s[int(x):int(y)+1])
    elif op == "replace":
        s = s[:int(x)] + cmd[3] + s[int(y)+1:]
    else:
        s = s[:int(x)] + s[int(x):int(y)+1][::-1] + s[int(y)+1:]