n = input()
for i in range(8):
    eq = n[0]
    for j in range(3):
        if (i >> j) & 1:
            op = "+"
        else:
            op = "-"
        eq += op + n[j+1]
    if eval(eq) == 7:
        print(eq + "=7")
        exit()
