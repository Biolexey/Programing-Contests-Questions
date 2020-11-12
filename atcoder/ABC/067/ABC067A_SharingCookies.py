a, b = map(int, input().split())
if a + b < 3:
    print("Impossible")
    exit()
print("Possible" if not a%3 or not b%3 or not (a+b)%3 else "Impossible")