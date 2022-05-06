#自分の回答
w = input()
while len(w) > 0:
    a = w[0]
    if w.count(a)%2 != 0:
        print("No")
        exit()
    w = w.replace(a,"")
print("Yes")

#奇抜な回答
s=input()
print("YNeos"[any(s.count(i)%2 for i in s)::2])

#ほかの回答
s = input()
f = True
for i in set(s):
    if s.count(i) % 2 : f = False
print('Yes' if f else 'No')