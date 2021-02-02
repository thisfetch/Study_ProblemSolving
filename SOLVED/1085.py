x, y, w, h = map(int,input().split())

if x > w - x:
    xshort = w - x
elif x <= w - x:
    xshort = x

if y > h - y:
    yshort = h - y
elif y <= h - y:
    yshort = y 

print(min(xshort, yshort))