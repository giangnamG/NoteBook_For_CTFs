def Euclid_Extended(a, b):
    r0, r1 = a, b
    q1, r2 = r0//r1, r0%r1
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    x2, y2 = x0 - x1*q1, y0 - y1*q1
    while r2 != 0:
        x0, x1 = x1, x2
        y0, y1 = y1, y2
        r0, r1 = r1, r2
        q1, r2 = r0//r1, r0%r1
        x2, y2 = x0 - x1*q1, y0 - y1*q1
    return r1, x1, y1

res = Euclid_Extended(29,8)
print(res)
#res = (1, -3, 11)
        