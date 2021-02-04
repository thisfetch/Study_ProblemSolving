N = int(input())
li = list(map(int, input().split()))
S = int(input())
i = 0
for _ in range(S):
    li[i], li[i + 1] = li[i + 1], li[i]
    i = i + 2

print(' '.join(map(str, li)))

