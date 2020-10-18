from collections import deque

ops = {"insert": deque.appendleft,
       "delete": lambda deq, x: deq.remove(x) if x in deq else None,
       "deleteF": deque.popleft,
       "deleteL": deque.pop}

deq = deque()
for _ in range(int(input())):
    com = input()#ここで.split()するとTLEになってしまう
    if com[6] != " ":
        ops[com[:7]](deq)
    else:
        ops[com[:6]](deq, com[7:])
print(*deq)
