import cmath

def koch(n, a1, a2):
    if not n:
        return None
    s = (a1*2 + a2) / 3
    t = (a1 + a2*2) / 3
    u = s + cmath.rect(1, cmath.pi/3) * (t-s)
    koch(n-1, a1, s)
    print(s.real, s.imag)
    koch(n-1, s, u)
    print(u.real, u.imag)
    koch(n-1, u, t)
    print(t.real, t.imag)
    koch(n-1, t, a2)

a1, a2 = 0j, 100+0j
print(a1.real, a1.imag)
koch(int(input()), a1, a2)
print(a2.real, a2.imag)