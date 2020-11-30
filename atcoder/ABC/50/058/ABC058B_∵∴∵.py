from collections import deque
O = deque(input())
E = deque(input())
ans = ""
while O or E:
    if O:
        ans += O.popleft()
    if E:
        ans += E.popleft()

print(ans)
