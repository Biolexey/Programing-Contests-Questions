h, w = map(int, input().split())

def cut(H, W):
    sum = H*W
    if not H%2 or not W%2:
        x = H*W//2
        return x, x
    else:
        x = max(H*(W//2), (H//2)*W)
        return x, sum-x

ans = 10**9

for i in range(2):
    h1 = h//3 + i
    area = [h1*w]
    H = h-h1
    area += cut(H, w)
    ans = min(ans, max(area)-min(area))

for i in range(2):
    w1 = w//3 + i
    area = [w1*h]
    W = w-w1
    area += cut(h, W)
    ans = min(ans, max(area)-min(area))

print(ans)