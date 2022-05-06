n = input()
for i in range(2):
    if n[i] == n[i+1] == n[i+2]:
        print("Yes")
        exit()
print("No")