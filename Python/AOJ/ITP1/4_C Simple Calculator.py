while 1:
    s = input()
    if "?" in s:
        exit()
    print(int(eval(s)))