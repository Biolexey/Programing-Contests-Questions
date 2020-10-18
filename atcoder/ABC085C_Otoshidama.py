#自分の回答
N, Y = map(int, input().split())
ans = []
#print((a,b,c if 10000*a + 5000*b + 1000*c == Y for a in range(N+1) for b in range(N-a+1) for c in range(N^a^b+c)))
#ギブアップ

#簡潔
N, Y = map(int, input().split())
for x in range(N+1):
    for y in range(N-x+1):
        z = N-x-y
        if 0 <= z <= 2000 and 10000*x + 5000*y + 1000*z == Y:
            print(x,y,z)
            exit()
print(-1,-1,-1)