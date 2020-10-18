#自分の回答
a, b = map(int,input().split())
c = a * b
if c % 2 == 0:
    print("Even")
else:
    print("Odd")

#簡潔
a, b = map(int, input().split())
print("Even" if a * b % 2 == 0 else "Odd")

