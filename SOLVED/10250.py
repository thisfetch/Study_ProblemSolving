num = int(input())

for _ in range(num):
    H, W, N = map(int,input().split())
    floor = N % H
    ho = N // H + 1
    if floor == 0:
        floor = H
        ho -= 1

    print(floor * 100 + ho)
