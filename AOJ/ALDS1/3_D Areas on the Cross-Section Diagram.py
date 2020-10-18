down, ponds = [], []

for i, j in enumerate(input()):
  if j == "\\":
    down.append(i)
  elif j == "/" and down:
    i_down = down.pop()
    area = i - i_down
    while ponds and ponds[-1][0] > i_down:
      area += ponds.pop()[1]
    ponds.append([i_down, area])
print(sum(p[1] for p in ponds))
print(len(ponds), *(p[1] for p in ponds))