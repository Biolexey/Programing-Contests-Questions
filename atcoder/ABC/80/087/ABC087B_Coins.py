a, b, c, X = [int(input()) for _ in range(4)]
print(sum(500*x + 100*y + 50*z == X for x in range(a+1) for y in range(b+1) for z in range(c+1)))
