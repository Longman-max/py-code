def vel(u, q, s):
    result = ((u * u) - (2 * q * s)) ** (1/2)
    print("V =", result)
    return

print("To find velocity;")
u = int(input("Input u: "))
q = int(input("Input q: "))
s = int(input("Input s: "))
vel(u, q, s)

def algebra(m, y):
    import math
    ans = (y + m) * (y + m)
    print("N =", (y + m) + math.sqrt(ans) + (4 * (m ** 2)) / 2)
    return

m = int(input("Input m: "))
y = int(input("Input y: "))
algebra(m, y)



def algebra3(v, t, w):
    print("U =", 1 - (3 * v))
    return

v = int(input("Input v: "))
t = int(input("Input t: "))
w = int(input("Input w: "))
algebra3(v, t, w)

def algebra4(u, f, g):
    import math
    result = (u / ((1 / f) + (1 / g)))
    print("T =", math.sqrt(result))
    return

u = int(input("Input u: "))
f = int(input("Input f: "))
g = int(input("Input g: "))

algebra4(u, f,g)

def algebra5(d, m, t, p):
    print((m * t) / (d * m + p))
    return

d = int(input("Input d: "))
m = int(input("Input m: "))
t = int(input("Input t: "))
p = int(input("Input p: "))

algebra5(d, m, t, p)