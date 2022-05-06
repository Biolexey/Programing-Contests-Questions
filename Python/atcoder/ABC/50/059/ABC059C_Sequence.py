n = int(input())
num = [*map(int, input().split())]

def calc(x, A):
    cnt = 0
    sum = 0
    for i in range(len(A)):
        if i % 2 == x:
            if sum + A[i] >= 0:#合計が負にならないとき
                cnt += A[i] + sum + 1
                sum = -1#合計は-1にする
            else:
                sum += A[i]

        if i % 2 == abs(x-1):
            if sum + A[i] <= 0:#合計が正にならないとき
                cnt += -(A[i] + sum) + 1
                sum = 1#合計は1にする
            else:
                sum += A[i]
    return cnt

print(min(calc(0, num), calc(1, num)))

            
            
