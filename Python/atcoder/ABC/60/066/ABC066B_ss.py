s = input()
cnt = 0
if len(s) % 2 == 1:
    s = s[:len(s)-1]
    cnt += 1
while s:
    if s[:(len(s)//2)] == s[len(s)//2:] and cnt != 0:
        print(len(s))
        break
    s = s[:len(s)-2]
    cnt += 1