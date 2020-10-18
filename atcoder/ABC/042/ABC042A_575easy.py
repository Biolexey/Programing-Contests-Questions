#自分の回答
a = list(map(int, input().split()))
if a.count(5) == 2 and a.count(7) == 1:
    print("YES")
else:
    print("NO")

#簡潔
abc = list(map(int, input().split()))
print("YES" if abc.count(5) == 2 and abc.count(7) == 1 else "NO")  