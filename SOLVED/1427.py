N = int(input())
A = list(map(int, str(N)))
A.sort(reverse=True)

for i in A:
    print(i, end="")