n = input()
s = 0
for i in range(len(n)):
    s += int(n[i])
print("Yes" if int(n) % s == 0 else "No")

#これでも可
n=input()
print("No" if int(n)%sum(map(int,n)) else "Yes")