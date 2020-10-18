s = input()
if len(s) %2 == 0 and s[0] == s[-1] or s[0] != s[-1] and len(s) %2 != 0:
    print("First")
else:
    print("Second")

#簡潔
s = input()
print("First" if len(s)%2 == (set(s[0],s[-1])%2) else "Second")