num = int(input())
arr = []

for _ in range(num):
    (x, y) = list(map(int,input().split()))
    arr.append((x, y))

arr = sorted(arr)

for i in arr:
    print(i[0], i[1])