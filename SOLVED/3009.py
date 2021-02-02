x = []; y = []

for _ in range(3):
    a, b = input().split()
    x.append(a)
    y.append(b)

if x[0] == x[1]:
    x.append(int(x[2]))
elif x[1] == x[2]:
    x.append(int(x[0]))
elif x[0] == x[2]:
    x.append(int(x[1]))

if y[0] == y[1]:
    y.append(int(y[2]))
elif y[1] == y[2]:
    y.append(int(y[0]))
elif y[0] == y[2]:
    y.append(int(y[1]))

print(x[3], y[3])
