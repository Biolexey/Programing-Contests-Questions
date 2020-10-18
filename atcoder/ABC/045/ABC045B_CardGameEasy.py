#自分の回答
a, b, c = input(), input(), input()
ref = a[0]
a = a[1:]
if len(a) == 0:
    print("A")
    exit()
for _ in range(len(a)+len(b)+len(c)):
    if ref == "a":
        if len(a) == 0:
            print("A")
            exit()
        ref = a[0]
        a = a[1:]

    elif ref == "b":
        if len(b) == 0:
            print("B")
            exit()
        ref = b[0]
        b = b[1:]
        
    else:
        if len(c) == 0:
            print("C")
            exit()
        ref = c[0]
        c = c[1:]
        
#わざとエラー吐かせる処理
a,b,c = [input() for i in range(3)]
sa = 'a'
for i in range(1796):
  try:
    if sa ==  'a':
      sa = a[0]
      a = a[1:]
 
    elif sa ==  'b':
      sa = b[0]
      b = b[1:]
 
    elif sa ==  'c':
      sa = c[0]
      c = c[1:]
  except:
    print(sa.upper())
    break




