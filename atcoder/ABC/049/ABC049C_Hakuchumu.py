# #自分の回答
# s = input()
# words = ["dreamer", "dream", "eraser", "erase"]
# while len(s) > 0:
#     match = [s.endswith(i) for i in words]
#     if True in match:
#         ans = words[match.index(True)]
#         s = s[:-len(ans)]
#         if len(s) == 0:
#             print("YES")
#             break
    
#     else:
#         print("NO")
#         break

#ほかの回答
s = input()


def solve(query):
    while 1:
        for frag in ("erase", "eraser", "dream", "dreamer"):
            if query.endswith(frag):
                query = query[:-len(frag)]
                break
        else:
            print("NO")
            break
        if not query:
            print("YES")
            break



solve(s)

