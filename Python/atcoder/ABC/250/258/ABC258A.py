k = int(input())
h, m = 21, 0

h += k//60
m += k%60

if len(str(m)) == 1:
    m = "0"+str(m)
    
print(f"{h}:{m}")
