while 1:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    print("#"*w)
    for _ in range(h-2):
        print("#"+"."*(w-2) + "#")
    print("#"*w)
    print()

#別解
while True:

    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for k in range(W):
            if i == 0 or i == H-1 or k == 0 or k == W-1:
                print("#",end = "")
            else:
                print(".",end = "")
        print()

    print() 