import sys
w = input()
print(sys.stdin.read().lower().split().count(w))

#リストに格納してもよし
li = []
while 1:
    t = input()
    if t == "END_OF_TEXT":
        break
    li.append(t.lower().split())
print(li.count(w))