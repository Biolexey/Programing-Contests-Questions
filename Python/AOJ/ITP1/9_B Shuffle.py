while 1:
    s = input()
    if s == "-":
        break
    m = int(input())
    for _ in range(m):
        h = int(input())
        s_back = s[:h]
        s_front = s[h:]
        s = s_front + s_back
    print(s)