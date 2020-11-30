s = input()
 
first = s.index('A')
end = s.rindex('Z')
 
ans = end - first + 1
print(ans)

s = input()
start = s.find('A')
end = s.rfind('Z',start)
print(end - start + 1)