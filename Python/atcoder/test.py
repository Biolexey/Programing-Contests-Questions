h1, h2, h3, w1, w2, w3 = map(int, input().split())

if h1+h2+h3 != w1+w2+w3:
    print(0)
    exit()
ans  =0
for i in range(1, w1-1):
    for j in range(1, w1-1-i):
        for k in range(1, w1-1-i-j):
            for l in range(1, w2-1):
                for m in range(1, w2-1-l):
                    for n in range(1, w2-1-l-m):
                        for o in range(1, w3-1):
                            for p in range(1, w3-1-o):
                                for q in range(1, w3-1-o-p):
                                    if i+l+o == h1 and j+m+p == h2 and k+n+q == h3:
                                        ans += 1

print(ans)