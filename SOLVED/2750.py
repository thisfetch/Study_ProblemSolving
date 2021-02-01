num = int(input())
arr = []
for i in range(num):
    arr.append(map(list(int, input()))

for i in range(len(arr)):
    for j in range(i + 1, num):
        arr[i], arr[j] = arr[j], arr[i]

print(arr)