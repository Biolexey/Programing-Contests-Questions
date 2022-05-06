d = set()
for _ in range(int(input())):
    command, num = input().split()
    if command == "insert":
        d.add(num)
    else:
        print("yes" if num in d else "no")
