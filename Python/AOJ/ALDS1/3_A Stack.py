#自分の解答(eval関数を使った)
stack = []
for a in input().split():
    if a.isdigit():
        stack.append(a)
    else:
        stack.append(str(eval("".join(reversed([stack.pop(), a, stack.pop()])))))
print(stack.pop())

#別解(dictのlambda関数を用いた)
ops = {"+":lambda x,y: y+x, "-":lambda x,y: y-x, "*":lambda x,y: y*x}
stack = []
for a in input().split():
    stack.append(ops[a](stack.pop(), stack.pop()) if a in ops else int(a))
print(stack.pop())