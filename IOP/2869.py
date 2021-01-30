A, B, V = map(int, input().split())
limit = A - B

if (V - A) % limit != 0:
    day = (V - A) / limit + 2
    print(int(day))
else:
    day = (V - A) / limit + 1
    print(int(day))
