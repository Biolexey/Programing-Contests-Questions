# n, k = map(int, input().split())
# l = [[0] for i in range(k)]
# min = 0
# a = sorted([int(input()) for _ in range(n)], reverse=True)
# for j in range(n):
#     l[min].append(a[j])
#     summin = 10**19
#     for i in range(k):
#         if summin > sum(l[i]):
#             summin = sum(l[i])
#             min = i
# print(l)
# print(max(sum(l[i]) for i in range(k)))

def check_p(p):
    global k, ws
    lt, nt = 0, 1  # loadage_of_current_truck, num_of_truck
    for w in ws:
        lt += w
        if lt > p:
            nt += 1
            if nt > k:
                return False
            lt = w
    return True


n, k = map(int, input().split())

ws = [int(input()) for _ in range(n)]
l, r, p = max(ws), sum(ws), 0

while l < r:
    p = (l + r) // 2
    if check_p(p):
        r = p
    else:
        l = p = p + 1

print(p)

