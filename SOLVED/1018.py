N, M = map(int, input().split())
chess = []
count = []

for _ in range(N):
    chess.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        a = 0
        b = 0
        for k in range(i, i + 8):
            for m in range(j, j + 8):
                if (k + m) %2 == 0:
                    if chess[k][m] != 'W':
                        a += 1
                    if chess[k][m] != 'B':
                        b += 1
                else:
                    if chess[k][m] != 'B':
                        a += 1
                    if chess[k][m] != 'W':
                        b += 1
        count.append(a)
        count.append(b)

print(min(count))